#!/bin/python33

import sys, json
import argparse
import glob
import os


def match_keys(keys: list, json_object: list) -> bool:
    return set(keys) == set(json_object.keys())


def is_list_of_strings(ll: list) -> bool:
    return all(map(lambda x: isinstance(x, str), ll))


def is_flow(flow) -> bool:
    return isinstance(flow, list) and \
        all(map(lambda x: isinstance(x, str), flow))


def is_list_of_flows(ll: list) -> bool:
    return all(map(lambda x: is_flow(x), ll))


def is_pattern(json_obj) -> bool:
    assert match_keys(['vulnerability', 'sources', 'sanitizers', 'sinks', 'implicit'], json_obj), set(json_obj.keys())
        
    assert isinstance(json_obj['vulnerability'], str), json_obj['vulnerability']
        
    assert isinstance(json_obj['sources'], list), json_obj['sources']
    assert is_list_of_strings(json_obj['sources']), json_obj['sources']

    assert isinstance(json_obj['sanitizers'], list), json_obj['sanitizers']
    assert is_list_of_strings(json_obj['sanitizers']), json_obj['sanitizers']

    assert isinstance(json_obj['sinks'], list), json_obj['sinks']
    assert is_list_of_strings(json_obj['sinks']), json_obj['sinks']

    assert isinstance(json_obj['implicit'], str), json_obj['implicit']
    assert json_obj['implicit'] in ["yes", "no"], json_obj['implicit']

    return True


def is_vulnerability(json_obj) -> bool:
    assert match_keys(['vulnerability', 'source', 'sink', 'unsanitized flows', 'sanitized flows'], json_obj), set(json_obj.keys())
        
    assert isinstance(json_obj['vulnerability'], str), json_obj['vulnerability']
        
    assert isinstance(json_obj['source'], str), json_obj['source']

    assert isinstance(json_obj['sink'], str), json_obj['sink']

    assert isinstance(json_obj['unsanitized flows'], str), json_obj['unsanitized flows']
    assert json_obj['unsanitized flows'] in ["yes", "no"], json_obj['unsanitized flows']

    assert isinstance(json_obj['sanitized flows'], list), json_obj['sanitized flows']
    assert is_list_of_flows(json_obj['sanitized flows']), json_obj['sanitized flows']

    return True
    

def is_same_vulnerability(v1, v2) -> bool:
    return v1['vulnerability'] == v2['vulnerability'] and \
        v1['source'] == v2['source'] and \
        v1['sink'] == v2['sink'] and \
        v1['unsanitized flows'] == v2['unsanitized flows'] and \
        set(list(map(frozenset, v1['sanitized flows']))) == set(list(map(frozenset, v2['sanitized flows'])))


def is_vulnerability_in_target(vulnerability, target_list):
    for v in target_list:
        if is_same_vulnerability(vulnerability, v):
            target_list.remove(v)
            return True, target_list

    return False, target_list



def validate_patterns_file(filename: str) -> bool:
    with open(filename, 'r') as f:
        patterns_list = json.loads(f.read())
    assert isinstance(patterns_list, list)

    for json_obj in patterns_list:
        assert is_pattern(json_obj)
   

def validate_output_file(filename: str):
    with open(filename, 'r') as f:
        output_list = json.loads(f.read())
    assert isinstance(output_list, list)

    for json_obj in output_list:
        assert is_vulnerability(json_obj)


def check_output(obtained, target):
    good = []
    missing = []

    with open(obtained, 'r') as f:
        output_list = json.loads(f.read())
    
    with open(target, 'r') as f:
        target_list = json.loads(f.read())

    for output in output_list:
        res, target_list = is_vulnerability_in_target(output, target_list)
        if res:
            good.append(output)
        else:
            missing.append(output)


    # print(f"{'*' * 40}\nGOOD FLOWS\n{good}")
    print(f"{'*' * 4}")
    if missing:
        print(f"\nMISSING FLOWS\n{missing}")
    if target_list:
        print(f"\nWRONG FLOWS\n{target_list}")
    if not missing and not target_list:
        print("ALL GOOD")



parser = argparse.ArgumentParser()
parser.add_argument("--pattern", '-p', help="Validate <pattern> file", default = False)
parser.add_argument("--output", '-o', help="Validate <output> file", default = False)
parser.add_argument("--target", '-t', help="Check <output> vs <target_file>", default = False)
parser.add_argument("--ast", '-a', help="ast dir", default = False)

args=parser.parse_args()

if vars(args)['output']:
    for output in glob.glob(f"{vars(args)['output']}/*"):
        validate_output_file(f"{output}")

if vars(args)['pattern']:
    ast_files = sorted(glob.glob(f"{vars(args)['ast']}/*"))
    pattern_files = sorted(glob.glob(f"{vars(args)['pattern']}/*"))
    os.system(f"rm {vars(args)['target']}/*")
    for f_pattern in pattern_files:
        # print(f_pattern)
        validate_patterns_file(f"{f_pattern}")

        # run examples
        slice_name = ast_files[pattern_files.index(f_pattern)]
        # slice_name = f_pattern.replace("patterns/", "").replace(".pattern", "")
        # print(f"Slice name: {slice_name}")
        print(f"++++ Slice {slice_name} Pattern {f_pattern}  ++++")

        os.system(f"python3 php-analyser.py {slice_name} {f_pattern} > /dev/null 2>&1")

if vars(args)['output'] and vars(args)['target']:
    target_files = sorted(glob.glob(f"{vars(args)['target']}/*"))
    for target in target_files:
        # validate_output_file(f"{target}")
        
        output_name = target.replace(f"{vars(args)['target']}/", f"{vars(args)['output']}/")
        print(f"\n=== TARGET {target} OUTPUTMATCH {output_name}  ===\n")
        check_output(f"{output_name}", f"{target}")

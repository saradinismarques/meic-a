import json
import sys
import os
from static_analysis import Static_Analysis

'''
Keep global dict with object variable.

visitor for each node type
assignment check source + uninitialized -> tainted
function call, check arguments for tainted vars -> vuln sink

Log global records of possible flows and match patterns in the end

class variable:
    name = string
    type = (tainted, sanitized, normal)
    source = (one from global sources list)
    sanitization function = ...

'''

patterns = []
sources = []
sinks = []
sanitizers = []

def main():
    global patterns, sources, sinks, sanitizers
    ast_path = sys.argv[1]
    patterns_path = sys.argv[2]
    
    ast_file = open(ast_path, 'r')
    ast = json.load(ast_file)

    patterns_file = open(patterns_path, 'r')
    patterns = json.load(patterns_file)

    output_path = "./output/" + ast_path.split("/")[1].replace("json","output.json")
    if not os.path.exists(os.path.dirname(output_path)) :
        os.makedirs(os.path.dirname(output_path))
        
    output_list = []
    for pattern in patterns :
        # print("----------------------------------> ", pattern)
        static_analysis = Static_Analysis(ast, pattern)
        output = static_analysis.analyse()
        output_list.extend(output)
        
    # print(json.dumps(output_list, indent=4))
    
    # output file
    result = json.dumps(output_list, indent=4)
    with open(output_path, "w") as outfile :
        outfile.write(result)

if __name__ == '__main__':
    main()



#!/bin/bash

dir="$(dirname "$(realpath "$0")")"
testsdir="$dir/tests"

function alltests {
    for test in "$testsdir"/* ; do
        echo "$(basename "$test")"
    done
}

# Create output directory if it does not exist
if [ ! -d "output" ]; then
    mkdir "output"
fi

for test in `alltests` ; do
    test_ast="tests/$test/$test.json"
    test_pattern="tests/$test/$test.patterns.json"
    outbase="output/$test"

    # FIXME: Uncomment the line to run YOUR project (if needed)
    exec="python3 php-analyser.py ${test_ast} ${test_pattern}"
    #exec="java -jar php-analyser.java ${test_ast} ${test_pattern}"
    #exec="php php-analyser.php ${test_ast} ${test_pattern}"
    #exec="node.exe php-analyser.js ${test_ast} ${test_pattern}"

    echo "Running test $test"
    timeout -v 300 $exec

done

echo -n "Check solution? (y/n)"
read answer

# Assert that all tests have been outputted to the output/ folder
for test in `alltests` ; do
    out="output/$test.output.json"
    if [ ! -f "$out" ]; then
        echo "Error: Test $test did not output anything. Expected output in $out"
        exit 1
    fi

    # Check output format
    if ! python3 validate.py -p tests/$test/$test.patterns.json -o output/$test.output.json; then
        echo "Error: Output $test.output.json has the wrong format."
        exit 1
    fi

    if [ "$answer" == "y" ]; then
        echo "Checking Test $test:"
        python3 validate.py -o output/$test.output.json -t tests/$test/$test.output.json
    fi

done

echo "All tests ran successfully!"

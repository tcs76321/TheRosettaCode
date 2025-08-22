#!/bin/bash
set -e  # Exit on any error

PROBLEM_DIR=$1
cd "$PROBLEM_DIR"

# Read the test cases and loop through them
TEST_CASES=$(python -c "import json; data=json.load(open('test_cases.json')); print(len(data['test_cases']))")
echo "Running $TEST_CASES tests for Python..."

for (( i=0; i<$TEST_CASES; i++ )); do
    INPUT=$(python -c "import json; data=json.load(open('test_cases.json')); print(data['test_cases'][$i]['input'])")
    EXPECTED=$(python -c "import json; data=json.load(open('test_cases.json')); print(data['test_cases'][$i]['expected'])")

    # Call the implementation and capture the result
    ACTUAL=$(python -c "from implementation import fizzbuzz; print(fizzbuzz($INPUT))")

    # Compare and throw an error if they don't match
    if [ "$ACTUAL" != "$EXPECTED" ]; then
        echo "TEST FAILED:"
        echo "  Input:    $INPUT"
        echo "  Expected: $EXPECTED"
        echo "  Actual:   $ACTUAL"
        exit 1
    fi
done

echo "All tests for Python passed!"
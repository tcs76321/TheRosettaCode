#!/bin/bash
set -e  # Exit on any error

PROBLEM_DIR=$1
cd "$PROBLEM_DIR/python"

# Get the problem name from the directory name
PROBLEM_NAME=$(basename "$PROBLEM_DIR")

echo "Running Python tests for $PROBLEM_NAME..."

# Use Python to run the tests
python3 -c "
import json
import sys
import os

# Add the current directory to Python path
sys.path.insert(0, '.')

# Import the implementation
try:
    # Import the module (e.g., fibonacci)
    impl_module = __import__('$PROBLEM_NAME')
    # Get the function (assumes function name matches module name)
    impl_function = getattr(impl_module, '$PROBLEM_NAME')
except ImportError as e:
    print(f'Failed to import implementation: {e}')
    sys.exit(1)
except AttributeError as e:
    print(f'Function $PROBLEM_NAME not found in module: {e}')
    sys.exit(1)

# Load test cases
try:
    with open('../test_cases.json', 'r') as f:
        test_data = json.load(f)
except FileNotFoundError:
    print('Error: test_cases.json not found')
    sys.exit(1)

all_passed = True

for test_case in test_data.get('test_cases', []):
    try:
        # Run the test
        result = impl_function(test_case['input'])
        expected = test_case['expected']
        
        if result != expected:
            print(f'FAIL: {test_case.get(\"name\", \"Unnamed test\")}')
            print(f'  Input:    {test_case[\"input\"]}')
            print(f'  Expected: {expected}')
            print(f'  Got:      {result}')
            all_passed = False
            
    except Exception as e:
        print(f'ERROR in test: {test_case.get(\"name\", \"Unnamed test\")} - {e}')
        all_passed = False

sys.exit(0 if all_passed else 1)
"
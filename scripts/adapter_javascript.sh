#!/bin/bash
set -e

PROBLEM_DIR=$1
cd "$PROBLEM_DIR"

# Use Node.js to parse the JSON and run the tests
node -e "
const testData = require('./test_cases.json');
const { fizzbuzz } = require('./implementation.js');

let allPassed = true;
console.log('Running ' + testData.test_cases.length + ' tests for Node.js...');

testData.test_cases.forEach((testCase, index) => {
    const actual = fizzbuzz(testCase.input);
    if (actual !== testCase.expected) {
        console.error(\`TEST FAILED: \${testCase.name}\`);
        console.error(\`  Input:    \${testCase.input}\`);
        console.error(\`  Expected: \${testCase.expected}\`);
        console.error(\`  Actual:   \${actual}\`);
        allPassed = false;
    }
});

if (!allPassed) {
    process.exit(1);
} else {
    console.log('All tests for JavaScript passed!');
}
"
#!/bin/bash
LANGUAGE=$1
PROBLEM_DIR="./problems/$2"

echo "=== Testing $2 with $LANGUAGE ==="

case $LANGUAGE in
    "python")
        ./scripts/test_python.sh "$PROBLEM_DIR"
        ;;
    "node")
        ./scripts/test_node.sh "$PROBLEM_DIR"
        ;;
    "java")
        # You would create a test_java.sh script
        ./scripts/test_java.sh "$PROBLEM_DIR"
        ;;
    *)
        echo "Error: Unknown language '$LANGUAGE'"
        exit 1
        ;;
esac
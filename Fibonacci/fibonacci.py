#!/usr/bin/env python3
"""
Fibonacci Sequence
"""


def fibonacci(n):
    """
    This function prints the first n numbers of the fibonacci sequence to the standard output.
    Requirements: n must >= 0
    """

    def fib_print(x, y):
        print(str(x) + ": " + str(y))

    print("Fibonacci Sequence from 0 to " + str(n))

    prev = 0
    curr = 0

    fib_print(0, curr)
    curr += 1

    for i in range(n):
        fib_print(i+1, curr)
        temp = curr
        curr += prev
        prev = temp

    print("End of Fib Seq")


if __name__ == "__main__":
    # Call the function only if this module is executed as the main script.
    fibonacci(100)

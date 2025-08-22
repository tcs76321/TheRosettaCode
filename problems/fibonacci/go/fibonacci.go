package main

import (
	"fmt"
)

func fibonacci(n int) {
	fmt.Printf("Fibonacci Sequence from 0 to %d\n", n)

	fibPrint := func(x, y int) {
		fmt.Printf("%d: %d\n", x, y)
	}

	prev, curr := 0, 0

	fibPrint(0, curr)
	curr++

	for i := 0; i < n; i++ {
		fibPrint(i+1, curr)
		temp := curr
		curr += prev
		prev = temp
	}

	fmt.Println("End of Fib Seq")
}

func main() {
	fibonacci(10)
}

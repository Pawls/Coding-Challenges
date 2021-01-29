package main

import "fmt"

// fibonacci is a function that returns
// a function that returns an int.
func fibonacci() func() int {
	prev2,prev1 := 0, 1
	return func() int {
		fib := prev2
		prev2,prev1 = prev1, fib+prev1
		return fib
	}
}

func main() {
	f := fibonacci()
	for i := 0; i < 10; i++ {
		fmt.Println(f())
	}
}

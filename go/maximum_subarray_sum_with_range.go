package main

import (
	"fmt"
)

func MaximumSubarraySum(numbers []int) {
  // Solve using sliding window.
  // Look for first positive number, then add each subsequent number. Update maxsum as necessary.
  // If the sum becomes negative, we have a bad sequence. Move to the next positive number and repeat.
  left, right := 0, 0
  sum, maxsum := 0, 0
  for i:=0; i<len(numbers); i++ {
    if numbers[i] < 1 {continue}
    sum = 0
    for j:=i; j<len(numbers); j++ {
      sum += numbers[j]
      if sum < 1 {
        i = j
	break
      } else if sum > maxsum {
        maxsum = sum
        left, right = i, j+1
      }
    }
  }
  fmt.Println("Max sum:", maxsum, "Range:", numbers[left:right])
}

func main() {
	MaximumSubarraySum([]int{-2,1,2,-5,4,-1,2,3,-5,6})
	MaximumSubarraySum([]int{1,2,3,4,5,6,7})
	MaximumSubarraySum([]int{100,-100,2,3,4,5,6,7})
	MaximumSubarraySum([]int{2,3,4,5,6,7,-120,120})
	MaximumSubarraySum([]int{-1,-2,-3,-4,-5})
	MaximumSubarraySum([]int{})
}

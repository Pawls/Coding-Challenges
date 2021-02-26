package kata

func MaximumSubarraySum(numbers []int) int {
  // Solve using sliding window.
  // Look for first positive number, then add each subsequent number. Update maxsum as necessary.
  // If the sum becomes negative, we have a bad sequence. Move to the next positive number and repeat.
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
      }
    }
  }
  return maxsum
}
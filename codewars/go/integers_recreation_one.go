package kata

import "math"

func ListSquared(m, n int)  [][]int {
  result := [][]int{}
  sum := 0
  for i := m; i <= n; i++ {
    for j := 1; j <= i; j++ {
      if i % j == 0 {
        sum += j*j
      }
    }
    root_test := int(math.Sqrt(float64(sum)))
    if root_test * root_test == sum {
      result = append(result, []int{i, sum})
    }
    sum = 0
  }
  return result
}
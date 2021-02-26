package kata

import "math"

func DigPow(n, p int) int {
  var digits []int
  orig := n
  for n > 0 {
    digits = append(digits, n % 10)
    n /= 10
    p++
  }
  result := 0
  for _,val := range digits {
    p--
    result += int(math.Pow(float64(val), float64(p)))
  }

  k := 1
  for orig * k < result {
    k++
  }
 
  if orig * k == result {
    return k
  } else {
    return -1
  }
}
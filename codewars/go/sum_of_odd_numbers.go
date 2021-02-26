package kata

func RowSumOddNumbers(n int) int {
  val := 1
  for i := 0; i < n; i++ {
    val += 2 * i
  }
  sum := 0
  for j := 0; j < n; j++ {
    sum += val
    val += 2
  }
  return sum
}
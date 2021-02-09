package multiplicationtable

func MultiplicationTable(size int) [][]int {
  res := [][]int{}
  for i := 0; i < size; i++ {
    temp := []int{}
    for j := 1; j <= size; j++ {
      temp = append(temp, j + (i * j) )
    }
    res = append(res, temp)
  }
  return res
}
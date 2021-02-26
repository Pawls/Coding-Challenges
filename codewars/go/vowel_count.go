package kata

func GetCount(str string) (count int) {
  vowels := map[rune]int{'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
  count = 0
  for _,c := range str {
    if _,in := vowels[c]; in {
      count++
    }
  }
  return count
}
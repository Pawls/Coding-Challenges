package kata

func Tickets(peopleInLine []int) string {
  change := make(map[int]int)
  for _,bill := range peopleInLine {
    change[bill]++
    switch bill {
    case 50:
      if change[25] == 0 {
        return "NO"
      }
      change[25]--
    case 100:
      if change[50] > 0 && change[25] > 0 {
        change[50]--
        change[25]--
      } else if change[25] > 2 {
        change[25] -= 3
      } else {
        return "NO"
      }
    }
  }
  return "YES"
}

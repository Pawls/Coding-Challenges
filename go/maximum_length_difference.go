package kata

func MxDifLg(a1 []string, a2 []string) int {
  if len(a1) == 0 || len(a2) == 0 {return -1}
  max1 := 0
  min1 := len(a1[0])
  for _,w := range a1 {
    if len(w) > max1 {
      max1 = len(w)
    }
    if len(w) < min1 {
      min1 = len(w)
    }
  }
  
  max2 := 0
  min2 := len(a2[0])
  for _,w := range a2 {
    if len(w) > max2 {
      max2 = len(w)
    }
    if len(w) < min2 {
      min2 = len(w)
    }
  }
  xy := max2 - min1
  yx := max1 - min2
  
  if xy > yx {
    return xy
  }
  return yx
}
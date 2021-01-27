package kata

import "strings"

func Accum(s string) string {
  s = strings.ToLower(s)
  result := ""
  for i,c := range s {
    result += strings.ToUpper(string(c))
    for j:=1; j < i+1; j++ {
      result += string(c)
    }
    if i < len(s)-1 {
      result += "-"
    }
  }
  return result
}
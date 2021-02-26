package kata

import "strings"

func PartList(arr []string) string {
  results := ""
  for i:=1; i<len(arr); i++ {
    first := strings.Join(arr[:i], " ")
    second := strings.Join(arr[i:], " ")
    results += "(" + first + ", " + second + ")"
  }
  return results
}
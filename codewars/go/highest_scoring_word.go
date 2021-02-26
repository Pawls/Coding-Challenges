package kata

import "strings"

func High(s string) string {
  var score, high int = 0, 0
  result := ""
  for _,word := range strings.Split(s, " ") {
    for _,c := range word {
      score += int(c) - 96
    }
    if high < score {
      high = score
      result = word
    }
    score = 0
  }
  return result
}
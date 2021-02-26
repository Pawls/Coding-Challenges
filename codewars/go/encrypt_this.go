package kata

import (
  "fmt"
  "strings"
)

func EncryptThis(text string) string {
  words := strings.Split(text, " ")
  for i, w := range words {
    switch len(w) {
    case 0: continue
    case 1: words[i] = fmt.Sprint(rune(w[0]))
    case 2: words[i] = fmt.Sprint(rune(w[0])) + string(w[1:])
    default: words[i] = fmt.Sprint(rune(w[0])) + string(w[len(w)-1]) + string(w[2:len(w)-1]) + string(w[1])
    }
  }
  return strings.Join(words, " ")
}
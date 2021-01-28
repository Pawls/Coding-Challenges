package kata

import "strings"

func wave(words string) []string {
	var result = []string{}
  
  for i := 0; i < len(words); i++ {
    if words[i] != ' ' {
      result = append(result, words[:i]+strings.ToUpper(string(words[i]))+words[i+1:])
    }
  }
  return result
}
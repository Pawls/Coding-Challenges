package main

import (
	"golang.org/x/tour/wc"
	"strings"
)

func WordCount(s string) map[string]int {
	words := strings.Fields(s)
	var result = make(map[string]int)
	for _, word := range words {
		result[word]++
	}
	return result
}

func main() {
	wc.Test(WordCount)
}

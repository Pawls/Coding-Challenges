package kata

import (
	"fmt"
	"strings"
	"strconv"
	"sort"
)

func Stati(str string) string {
  if str == "" {return ""}
	words := strings.Split(str, ", ")
	mean := 0
	all_times := []int{}
	for _,w := range words {
		seconds := convertToSec(strings.Split(w, "|"))
		mean += seconds
		all_times = append(all_times, seconds)
	}
	sort.Ints(all_times)
	var s_median string
	s_range := convertToHms(all_times[len(all_times)-1] - all_times[0])
	s_mean := convertToHms(mean / len(words))
	if len(all_times) % 2 == 0 {
		s_median = convertToHms(int((all_times[len(all_times)/2] + all_times[len(all_times)/2 - 1])/2))
	} else {
		s_median = convertToHms(all_times[len(all_times)/2])
	}
	return fmt.Sprint("Range: ", s_range, " Average: ", s_mean, " Median: ", s_median)
}

func convertToSec(hms []string) int {
	hrs, _ := strconv.Atoi(hms[0])
	min, _ := strconv.Atoi(hms[1])
	sec, _ := strconv.Atoi(hms[2])

	return (60 * 60 * hrs) + (60 * min) + sec
}

func convertToHms(num int) string {
	sec := num % 60
	num /= 60
	min := num % 60
	num /= 60
	
	return fmt.Sprintf("%02d|%02d|%02d", num, min, sec)
}
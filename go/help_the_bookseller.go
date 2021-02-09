import(
  "strings"
  "fmt"
  "strconv"
)

func StockList(listArt []string, listCat []string) string {
  if len(listArt) == 0 || len(listCat) == 0 {
    return ""
  }

  res := make(map[string]int)

  for _, book := range listArt {
    stocked, _ := strconv.Atoi(strings.Split(book, " ")[1])
    res[string(book[0])] += stocked
  }

  res_str := []string{}
  for _, cat := range listCat {
    res_str = append(res_str, fmt.Sprintf("(%s : %d)", cat, res[cat]) )
  }

  return strings.Join(res_str, " - ")
}
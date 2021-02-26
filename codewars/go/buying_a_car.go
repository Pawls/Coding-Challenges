package kata

import "math"

func NbMonths(startPriceOld, startPriceNew, savingPerMonth int, percentLossByMonth float64) [2]int {
  oldPrice := float64(startPriceOld)
  newPrice := float64(startPriceNew)
  savings := 0
  for oldPrice + float64(savings) < newPrice {
    oldPrice-= (percentLossByMonth / 100.0) * oldPrice
    newPrice-= (percentLossByMonth / 100.0) * newPrice
    if savings % (savingPerMonth * 2) == 0 {
      percentLossByMonth += 0.5
    }
    savings += savingPerMonth
  }
  return [2]int{savings / savingPerMonth, int(math.Round(oldPrice + float64(savings) - newPrice))}
}
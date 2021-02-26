package main

import "golang.org/x/tour/pic"

func Pic(dx, dy int) [][]uint8 {
	grid := make([][]uint8, dy)
	for row := range grid {
		for col:=0;col<dx;col++{
			grid[row] = append(grid[row], uint8(row^col))
		}
	}
	return grid
}

func main() {
	pic.Show(Pic)
}

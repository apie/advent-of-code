package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func readContent(filename string) []byte {
	content, err := os.ReadFile(filename)
	if err != nil {
		fmt.Println(fmt.Printf("Could not read file %s", filename))
	}
	return content
}

func splitLines(content []byte) []string {
	return strings.Split(strings.TrimSpace(string(content)), "\n")
}

// type grid [3][7]bool
type grid [6][50]bool

func (g grid) print() {
	for y := range len(g) {
		for x := range len(g[0]) {
			if g[y][x] {
				fmt.Print("#")
			} else {
				fmt.Print(".")
			}
		}
		fmt.Print("\n")
	}
}
func (g grid) addRect(lx int, ly int) grid {
	fmt.Printf("> adding rect lx %d ly %d\n", lx, ly)
	for x := range lx {
		for y := range ly {
			g[y][x] = true
		}
	}
	return g
}
func (g grid) rotateCol(x int, dy int) grid {
	fmt.Printf("> rotating col x %d dy %d\n", x, dy)
	for i := 0; i < dy; i++ {
		var newcol []bool = nil
		for y := range len(g) {
			if y == 0 {
				newcol = append(newcol, g[len(g)-1][x])
			} else {
				newcol = append(newcol, g[y-1][x])
			}
		}
		for y, val := range newcol {
			g[y][x] = val
		}
	}
	return g
}
func (g grid) rotateRow(y int, dx int) grid {
	fmt.Printf("> rotating row y %d dx %d\n", y, dx)
	for i := 0; i < dx; i++ {
		var newrow []bool = nil
		for x := range len(g[0]) {
			if x == 0 {
				newrow = append(newrow, g[y][len(g[0])-1])
			} else {
				newrow = append(newrow, g[y][x-1])
			}
		}
		for x, val := range newrow {
			g[y][x] = val
		}
	}
	return g
}
func (g grid) numlit() int {
	numlit := 0
	for y := range len(g) {
		for x := range len(g[0]) {
			if g[y][x] {
				numlit++
			}
		}
	}
	return numlit
}
func numPixelsLit(lines []string) int {
	var g grid
	for _, line := range lines {
		fmt.Println(line)
		ops := strings.Split(line, " ")
		switch ops[0] {
		case "rect":
			{
				rectsize := strings.Split(ops[1], "x")
				x, _ := strconv.Atoi(rectsize[0])
				y, _ := strconv.Atoi(rectsize[1])
				g = g.addRect(x, y)
			}
		case "rotate":
			{
				if ops[1] == "column" {
					x, _ := strconv.Atoi(strings.Split(ops[2], "=")[1])
					dy, _ := strconv.Atoi(ops[4])
					g = g.rotateCol(x, dy)

				} else if ops[1] == "row" {
					y, _ := strconv.Atoi(strings.Split(ops[2], "=")[1])
					dx, _ := strconv.Atoi(ops[4])
					g = g.rotateRow(y, dx)
				}
			}
		default:
			fmt.Println("default")
		}
		g.print()
		fmt.Println("")
	}
	return g.numlit()
}
func D8a(filename string) int {
	return numPixelsLit(splitLines(readContent(filename)))
}

func D8b(filename string) int {
	return -1
}

func main() {
	filename := "d08.input"
	start := time.Now()
	elapsed := func() time.Duration {
		return time.Since(start).Round(time.Millisecond)
	}
	ansa := D8a(filename)
	fmt.Println("Part a: how many pixels should be lit:", ansa)
	fmt.Printf("Took %6s\n", elapsed())
	start = time.Now()
	ansb := D8b(filename)
	fmt.Println("Part b: :", ansb)
	fmt.Printf("Took %6s\n", elapsed())
}

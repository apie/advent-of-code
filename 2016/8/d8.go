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

const letterwidth = 5

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
	// fmt.Printf("> adding rect lx %d ly %d\n", lx, ly)
	for x := range lx {
		for y := range ly {
			g[y][x] = true
		}
	}
	return g
}
func (g grid) rotateCol(x int, dy int) grid {
	// fmt.Printf("> rotating col x %d dy %d\n", x, dy)
	for range dy {
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
	// fmt.Printf("> rotating row y %d dx %d\n", y, dx)
	for range dx {
		var newrow []bool = nil
		for x := range len(g[0]) {
			if x == 0 {
				newrow = append(newrow, g[y][len(g[0])-1])
			} else {
				newrow = append(newrow, g[y][x-1])
			}
		}
		copy(g[y][:], newrow)
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

func (g grid) runOperations(lines []string) grid {
	for _, line := range lines {
		// fmt.Println(line)
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
				switch ops[1] {
				case "column":
					x, _ := strconv.Atoi(strings.Split(ops[2], "=")[1])
					dy, _ := strconv.Atoi(ops[4])
					g = g.rotateCol(x, dy)

				case "row":
					y, _ := strconv.Atoi(strings.Split(ops[2], "=")[1])
					dx, _ := strconv.Atoi(ops[4])
					g = g.rotateRow(y, dx)
				}
			}
		default:
			fmt.Println("default")
		}
		// g.print()
		// fmt.Println("")
	}
	return g
}

func (g grid) getLetter() string {
	// Loop the y lines of the grid, but only for the width of one letter. Then compare with known letters and return the letter string if the letter was recognized.
	// letter_empty := [6]string{
	// 	".....",
	// 	".....",
	// 	".....",
	// 	".....",
	// 	".....",
	// 	".....",
	// }
	letterz := [6]string{
		"####.",
		"...#.",
		"..#..",
		".#...",
		"#....",
		"####.",
	}
	lettery := [6]string{
		"#...#",
		"#...#",
		".#.#.",
		"..#..",
		"..#..",
		"..#..",
	}
	letterl := [6]string{
		"#....",
		"#....",
		"#....",
		"#....",
		"#....",
		"####.",
	}
	letterj := [6]string{
		"..##.",
		"...#.",
		"...#.",
		"...#.",
		"#..#.",
		".##..",
	}
	letterp := [6]string{
		"###..",
		"#..#.",
		"#..#.",
		"###..",
		"#....",
		"#....",
	}
	letterh := [6]string{
		"#..#.",
		"#..#.",
		"####.",
		"#..#.",
		"#..#.",
		"#..#.",
	}
	letterr := [6]string{
		"###..",
		"#..#.",
		"#..#.",
		"###..",
		"#.#..",
		"#..#.",
	}
	letterc := [6]string{
		".##..",
		"#..#.",
		"#....",
		"#....",
		"#..#.",
		".##..",
	}
	letterk := [6]string{
		"#..#.",
		"#.#..",
		"##...",
		"#.#..",
		"#.#..",
		"#..#.",
	}
	var chararr [6]string
	for y := range len(g) {
		char := ""
		for _, x := range g[y][0:letterwidth] {
			if x {
				char += "#"
			} else {
				char += "."
			}
		}
		chararr[y] = char
	}
	letter := ""
	switch strings.Join(chararr[:], "") {
	case strings.Join(letterk[:], ""):
		{
			letter = "K"
		}
	case strings.Join(letterc[:], ""):
		{
			letter = "C"
		}
	case strings.Join(letterr[:], ""):
		{
			letter = "R"
		}
	case strings.Join(letterh[:], ""):
		{
			letter = "H"
		}
	case strings.Join(letterp[:], ""):
		{
			letter = "P"
		}
	case strings.Join(letterj[:], ""):
		{
			letter = "J"
		}
	case strings.Join(lettery[:], ""):
		{
			letter = "Y"
		}
	case strings.Join(letterl[:], ""):
		{
			letter = "L"
		}
	case strings.Join(letterz[:], ""):
		{
			letter = "Z"
		}
	default:
		{
			letter = "?"
		}
	}
	return letter
}

func (g grid) shiftLetter() grid {
	// Shift the grid one letter width to the right.
	for y := range len(g) {
		g = g.rotateRow(y, letterwidth)
	}
	return g
}

func numPixelsLit(lines []string) int {
	var g grid
	g = g.runOperations(lines)
	return g.numlit()
}

func D8a(filename string) int {
	return numPixelsLit(splitLines(readContent(filename)))
}

func D8b(filename string) string {
	var g grid
	g = g.runOperations(splitLines(readContent(filename)))
	var letters []string
	for range len(g[0]) / letterwidth {
		g = g.shiftLetter()
		letter := g.getLetter()
		// fmt.Printf("letter %s\n", letter)
		letters = append(letters, letter)
		// g.print()
	}
	// Concatenate the string in reverse order
	answer := ""
	for i := range letters {
		answer += letters[len(letters)-1-i]
	}
	return answer
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
	fmt.Println("Part b: what is the code on the screen:", ansb)
	fmt.Printf("Took %6s\n", elapsed())
}

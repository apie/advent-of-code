package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strconv"
	"strings"
)

func D1a(filename string) int {
	content, err := ioutil.ReadFile(filename) // the file is inside the local directory
	if err != nil {
		fmt.Println("Err")
	}
	x, y, angle := 0, 0, 0
	directions := strings.Split(strings.TrimSpace(string(content)), ", ")
	for _, element := range directions {
		nblocks, _ := strconv.Atoi(element[1:])
		fmt.Println(element, nblocks)
		if element[0] == 'L' {
			angle -= 90
		} else if element[0] == 'R' {
			angle += 90
		}
		if angle < 0 {
			angle += 360
		}
		angle = angle % 360
		if angle == 0 {
			// facing upwards
			y += nblocks
		}
		if angle == 90 {
			// facing right
			x += nblocks
		}
		if angle == 180 {
			// facing down
			y -= nblocks
		}
		if angle == 270 {
			// facing left
			x -= nblocks
		}
		fmt.Println(angle)
		fmt.Println(x)
		fmt.Println(y)
		fmt.Println()
	}

	return int(math.Abs(float64(x)) + math.Abs(float64(y)))
}

func D1b(filename string) int {
	content, err := ioutil.ReadFile(filename) // the file is inside the local directory
	if err != nil {
		fmt.Println("Err")
	}
	x, y, angle := 0, 0, 0
	var visited = make(map[string]bool)
	visited[fmt.Sprintf("%d,%d", x, y)] = true
	directions := strings.Split(strings.TrimSpace(string(content)), ", ")
	for _, element := range directions {
		nblocks, _ := strconv.Atoi(element[1:])
		fmt.Println(element, nblocks)
		if element[0] == 'L' {
			angle -= 90
		} else if element[0] == 'R' {
			angle += 90
		}
		if angle < 0 {
			angle += 360
		}
		angle = angle % 360
		for i := 1; i <= nblocks; i++ {
			if angle == 0 {
				// facing upwards
				y += 1
			} else if angle == 90 {
				// facing right
				x += 1
			} else if angle == 180 {
				// facing down
				y -= 1
			} else if angle == 270 {
				// facing left
				x -= 1
			}
			visitedStr := fmt.Sprintf("%d,%d", x, y)
			if visited[visitedStr] {
				fmt.Println("Visited before!")
				// Visited before. Return location
				return int(math.Abs(float64(x)) + math.Abs(float64(y)))
			}
			visited[visitedStr] = true
		}

		//fmt.Println(angle)
		//fmt.Println(x)
		//fmt.Println(y)
		//fmt.Println()
	}

	return 0
}
func main() {
	filename := "d1.input"
	ansa := D1a(filename)
	fmt.Println("Part a: Manhattan distance from start: ", ansa)
	ansb := D1b(filename)
	fmt.Println("Part b: Distance of first location visited twice: ", ansb)
}

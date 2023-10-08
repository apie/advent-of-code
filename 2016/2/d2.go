package main

import (
	"fmt"
	"os"
	"strings"
)

func D2a(filename string) string {
	keypad := [][]int{
		[]int{1, 2, 3},
		[]int{4, 5, 6},
		[]int{7, 8, 9},
	}
	startx := 1
	starty := 1
	return solve_keypad(filename, keypad, startx, starty)
}
func D2b(filename string) string {
	keypad := [][]int{
		[]int{0, 0, 1, 0, 0},
		[]int{0, 2, 3, 4, 0},
		[]int{5, 6, 7, 8, 9},
		[]int{0, 10, 11, 12, 0},
		[]int{0, 0, 13, 0, 0},
	}
	startx := 0
	starty := 2
	return solve_keypad(filename, keypad, startx, starty)
}
func solve_keypad(filename string, keypad [][]int, startx int, starty int) string {
	content, err := os.ReadFile(filename) // the file is inside the local directory
	if err != nil {
		fmt.Println("Err")
	}
	code := ""
	x := startx
	y := starty
	maxx := len(keypad[0]) - 1
	maxy := len(keypad) - 1
	lines := strings.Split(strings.TrimSpace(string(content)), "\n")
	for _, line := range lines {
		//fmt.Println(line)
		for _, char := range strings.Split(line, "") {
			//fmt.Println(char)
			if char == "U" {
				if y > 0 && keypad[y-1][x] > 0 {
					y -= 1
				}
			} else if char == "D" {
				if y < maxy && keypad[y+1][x] > 0 {
					y += 1
				}
			} else if char == "L" {
				if x > 0 && keypad[y][x-1] > 0 {
					x -= 1
				}
			} else if char == "R" {
				if x < maxx && keypad[y][x+1] > 0 {
					x += 1
				}
			}
			//fmt.Println(x*10+y)
		}
		code = fmt.Sprintf("%s%X", code, keypad[y][x])
		//fmt.Println(code)
	}
	return code
}

func main() {
	filename := "d2.input"
	ansa := D2a(filename)
	fmt.Println("Part a: bathroom code: ", ansa)
	ansb := D2b(filename)
	fmt.Println("Part b: bathroom code hex: ", ansb)
}

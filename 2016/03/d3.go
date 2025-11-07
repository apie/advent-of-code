package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func valid_triangle(a, b, c int) bool {
	if a+b <= c {
		return false
	}
	if a+c <= b {
		return false
	}
	if b+c <= a {
		return false
	}
	return true
}

func D3a(filename string) int {
	r_obj := regexp.MustCompile(`\s+`)
	content, err := os.ReadFile(filename)
	if err != nil {
		fmt.Println("Err")
	}
	n_possible := 0
	lines := strings.Split(strings.TrimSpace(string(content)), "\n")
	for _, line := range lines {
		//  fmt.Println(line)
		var sides [3]int
		i := -1
		for _, word := range strings.Split(strings.TrimSpace(r_obj.ReplaceAllString(line, " ")), " ") {
			word = strings.TrimSpace(word)
			//	fmt.Println(word)
			i += 1
			sides[i], _ = strconv.Atoi(word)
		}
		if valid_triangle(sides[0], sides[1], sides[2]) {
			//  fmt.Println("possible")
			n_possible += 1
		} else {
			//  fmt.Println("impossible")
		}
	}
	return n_possible
}

func D3b(filename string) int {
	r_obj := regexp.MustCompile(`\s+`)
	content, err := os.ReadFile(filename)
	if err != nil {
		fmt.Println("Err")
	}
	n_possible := 0
	lines := strings.Split(strings.TrimSpace(string(content)), "\n")
	line_no := 0
	var sides [3][3]int
	for _, line := range lines {
		//  fmt.Println(line)
		i := -1
		for _, word := range strings.Split(strings.TrimSpace(r_obj.ReplaceAllString(line, " ")), " ") {
			word = strings.TrimSpace(word)
			//	fmt.Println(word)
			i += 1
			sides[i][line_no], _ = strconv.Atoi(word)
		}
		if line_no == 2 {
			for _, tr := range sides {
				if valid_triangle(tr[0], tr[1], tr[2]) {
					//  fmt.Println("possible")
					n_possible += 1
				} else {
					//  fmt.Println("impossible")
				}
			}
			line_no = -1
		}
		line_no += 1
	}
	return n_possible
}

func main() {
	filename := "d3.input"
	ansa := D3a(filename)
	fmt.Println("Part a: how many listed triangles are possible: ", ansa)
	ansb := D3b(filename)
	fmt.Println("Part b: how many listed triangles are possible (vertically): ", ansb)
}

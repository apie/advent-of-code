package main

import (
	"fmt"
	"os"
	"slices"
	"strings"
)

func D2a(filename string) string {
	content, err := os.ReadFile(filename) // the file is inside the local directory
	if err != nil {
		fmt.Println("Err")
	}
	code := ""
	curnum := 5
	lines := strings.Split(strings.TrimSpace(string(content)), "\n")
	l := []int{1, 4, 7}
	r := []int{3, 6, 9}
	for _, line := range lines {
		fmt.Println(line)
		for _, char := range strings.Split(line, "") {
			//fmt.Println(char)
			if char == "U" && curnum-3 > 0 {
				curnum -= 3
			} else if char == "D" && curnum+3 < 10 {
				curnum += 3
				// need Go >= 1.21
			} else if char == "L" && !slices.Contains(l, curnum) {
				curnum -= 1
			} else if char == "R" && !slices.Contains(r, curnum) {
				curnum += 1
			}
		}
		code = fmt.Sprintf("%s%d", code, curnum)
		fmt.Println(code)
	}
	return code
}
func D2b(filename string) string {
	content, err := os.ReadFile(filename) // the file is inside the local directory
	if err != nil {
		fmt.Println("Err")
	}
	//    1
	//  2 3 4
	//5 6 7 8 9
	//  A B C
	//    D
	code := ""
	curnum := 5
	lines := strings.Split(strings.TrimSpace(string(content)), "\n")
	fmt.Println(lines)
	l := []int{1, 2, 5, 10, 13}
	r := []int{1, 4, 9, 12, 13}
	u := []int{5, 2, 1, 4, 9}
	d := []int{5, 10, 13, 12, 9}
	up2 := []int{3, 13}
	down2 := []int{1, 11}
	for _, line := range lines {
		fmt.Println(line)
		for _, char := range strings.Split(line, "") {
			// need Go >= 1.21
			if char == "U" && !slices.Contains(u, curnum) {
				if slices.Contains(up2, curnum) {
					curnum -= 2
				} else {
					curnum -= 4
				}
			} else if char == "D" && !slices.Contains(d, curnum) {
				if slices.Contains(down2, curnum) {
					curnum += 2
				} else {
					curnum += 4
				}
			} else if char == "L" && !slices.Contains(l, curnum) {
				curnum -= 1
			} else if char == "R" && !slices.Contains(r, curnum) {
				curnum += 1
			}
		}
		fmt.Println(curnum)
		code = fmt.Sprintf("%s%X", code, curnum) // Append hex representation of code
		fmt.Println(code)
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

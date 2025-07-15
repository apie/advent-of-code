package main

import (
	"fmt"
	"os"
	"sort"
	"strings"
	"time"
)

func getMostCommonLetters(word string) []string {
	// copied from D4
	/* Returns the most common letters in order. On ties it uses alphabetic order.*/
	m := make(map[string]int)
	for _, letter := range strings.Split(strings.ReplaceAll(word, "-", ""), "") {
		m[letter]++
	}
	// fmt.Println(len(m))
	// fmt.Println(m)
	mostCommon := make([]string, 0, len(m))

	for key := range m {
		mostCommon = append(mostCommon, key)
	}

	sort.SliceStable(mostCommon, func(i, j int) bool {
		if m[mostCommon[i]] == m[mostCommon[j]] {
			return mostCommon[i] < mostCommon[j]
		}
		return m[mostCommon[i]] > m[mostCommon[j]]
	})

	// for _, k := range mostCommon {
	//  fmt.Println(k, m[k])
	// }
	return mostCommon

}

func D6a(filename string) string {
	content, err := os.ReadFile(filename)
	if err != nil {
		fmt.Println(fmt.Printf("Could not read file %s", filename))
	}
	// Get most common character per column
	// First make list of columns
	var columns [8]string
	for _, line := range strings.Split(strings.TrimSpace(string(content)), "\n") {
		// fmt.Println(line)
		for colNum, char := range line {
			// fmt.Println(string(char))
			columns[colNum] += string(char)
		}
	}
	// fmt.Println("----")
	// fmt.Println(columns)
	answer := ""
	for _, column := range columns {
		if len(column) == 0 {
			continue
		}
		mc := getMostCommonLetters(column)
		// fmt.Println(mc)
		answer += mc[0]
	}
	// fmt.Println("--=-")
	return answer
}

func D6b(filename string) string {
	return "fail"
}

func main() {
	filename := "d06.input"
	start := time.Now()
	elapsed := func() time.Duration {
		return time.Since(start).Round(time.Millisecond)
	}
	ansa := D6a(filename)
	fmt.Println("Part a: Given the recording in your puzzle input, what is the error-corrected version of the message being sent?", ansa)
	fmt.Printf("Took %6s\n", elapsed())
	start = time.Now()
	ansb := D6b(filename)
	fmt.Println("Part b: :", ansb)
	fmt.Printf("Took %6s\n", elapsed())
}

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
	return mostCommon
}

func readContent(filename string) []byte {
	content, err := os.ReadFile(filename)
	if err != nil {
		fmt.Println(fmt.Printf("Could not read file %s", filename))
	}
	return content
}

func makeListOfColumns(content []byte) [8]string {
	// First make list of columns
	var columns [8]string
	for _, line := range strings.Split(strings.TrimSpace(string(content)), "\n") {
		for colNum, char := range line {
			columns[colNum] += string(char)
		}
	}
	return columns
}

func D6a(filename string) string {
	columns := makeListOfColumns(readContent(filename))
	answer := ""
	for _, column := range columns {
		if len(column) == 0 {
			continue
		}
		mc := getMostCommonLetters(column)
		answer += mc[0]
	}
	return answer
}

func D6b(filename string) string {
	columns := makeListOfColumns(readContent(filename))
	answer := ""
	for _, column := range columns {
		if len(column) == 0 {
			continue
		}
		mc := getMostCommonLetters(column)
		answer += mc[len(mc)-1]
	}
	return answer
}

func main() {
	filename := "d06.input"
	start := time.Now()
	elapsed := func() time.Duration {
		return time.Since(start).Round(time.Millisecond)
	}
	ansa := D6a(filename)
	fmt.Println("Part a: Given the recording in your puzzle input, what is the error-corrected version of the message being sent? (most common letter)", ansa)
	fmt.Printf("Took %6s\n", elapsed())
	start = time.Now()
	ansb := D6b(filename)
	fmt.Println("Part b: Given the recording in your puzzle input and this new decoding methodology, what is the original message that Santa is trying to send? (least common letter):", ansb)
	fmt.Printf("Took %6s\n", elapsed())
}

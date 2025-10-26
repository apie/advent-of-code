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

func get_decompress_len(inp string) int {
	l := 0
	q := strings.Split(inp, "")
	i := 0
	for i < len(q) {
		c := q[i]
		fmt.Println(c)
		if c == "(" {
			instr := ""
			for c != ")" {
				i++
				c = q[i]
				if c != ")" {
					instr += c
				}
			}
			fmt.Printf(">INSTR: %s\n", instr)
			repr1, _ := strconv.Atoi(strings.Split(instr, "x")[0])
			repr2, _ := strconv.Atoi(strings.Split(instr, "x")[1])
			fmt.Printf(">REPR1: %d\n", repr1)
			fmt.Printf(">REPR2: %d\n", repr2)
			l += repr1 * repr2
			i += repr1
		} else {
			l += 1
		}
		i++
	}
	fmt.Println("")
	return l
}

func get_decompress_len_inc_nested(inp string) int {
	l := 0
	q := strings.Split(inp, "")
	i := 0
	for i < len(q) {
		c := q[i]
		// fmt.Println(c)
		if c == "(" {
			instr := ""
			for c != ")" {
				i++
				c = q[i]
				if c != ")" {
					instr += c
				}
			}
			// fmt.Printf(">INSTR: %s\n", instr)
			repr1, _ := strconv.Atoi(strings.Split(instr, "x")[0])
			repr2, _ := strconv.Atoi(strings.Split(instr, "x")[1])
			// fmt.Printf(">REPR1: %d\n", repr1)
			// fmt.Printf(">REPR2: %d\n", repr2)
			data := ""
			for range repr1 {
				i++
				data += q[i]
			}
			// fmt.Printf("> data: %s\n", data)
			if strings.Contains(data, "(") {
				// processed_data = data*repr2
				processed_data := ""
				for range repr2 {
					processed_data += data
				}
				// fmt.Printf(">Getting ld for: %s\n", processed_data)
				ld := get_decompress_len_inc_nested(processed_data)
				// fmt.Printf(">ld: %d\n", ld)
				l += ld
			} else {
				l += repr1 * repr2
			}
		} else {
			l += 1
		}
		i++
	}
	// fmt.Printf(">L: %d\n", l)
	// fmt.Println("")
	return l
}

func D9a(filename string) int {
	return get_decompress_len(splitLines(readContent(filename))[0])
}

func D9b(filename string) int {
	return get_decompress_len_inc_nested(splitLines(readContent(filename))[0])
}

func main() {
	filename := "d09.input"
	start := time.Now()
	elapsed := func() time.Duration {
		return time.Since(start).Round(time.Millisecond)
	}
	ansa := D9a(filename)
	fmt.Println("Part a: Get decompressed length of the input string:", ansa)
	fmt.Printf("Took %6s\n", elapsed())
	start = time.Now()
	ansb := D9b(filename)
	fmt.Println("Part b: Get decompressed length of the input string, also parsing nested markers:", ansb)
	fmt.Printf("Took %6s\n", elapsed())
}

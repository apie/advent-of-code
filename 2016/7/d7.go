package main

import (
	"fmt"
	"os"
	"strings"
	"time"
)

const (
	OKGREEN = "\033[92m"
	WARNING = "\033[93m"
	FAIL    = "\033[91m"
	ENDC    = "\033[0m"
)

func ok(s string) string {
	return OKGREEN + s + ENDC
}
func warning(s string) string {
	return WARNING + s + ENDC
}
func fail(s string) string {
	return FAIL + s + ENDC
}
func color(b bool) string {
	if b {
		return ok("true")
	}
	return fail("false")
}
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

func supportsTLS(ip string) bool {
	var stack []rune
	foundAbba := false
	inbrack := false
	foundAbbaInbrack := false
	for _, c := range ip {
		if string(c) == "[" || string(c) == "]" {
			inbrack = !inbrack
			clear(stack)
			continue
		}
		if len(stack) == 4 {
			// shift to left
			stack[0] = stack[1]
			stack[1] = stack[2]
			stack[2] = stack[3]
			stack[3] = c
		} else {
			stack = append(stack, c)
		}
		if len(stack) == 4 {
			if stack[0] == stack[3] && stack[1] == stack[2] && stack[0] != stack[1] {
				if inbrack {
					foundAbbaInbrack = true
				} else {
					foundAbba = true
				}
			}
		}
	}
	supports := foundAbba && !foundAbbaInbrack
	fmt.Println(ip, "supports TLS:", color(supports))
	return supports
}

func getbab(aba string) string {
	return string(aba[1]) + string(aba[0]) + string(aba[1])
}
func supportsSSL(ip string) bool {
	abas := make(map[string]bool)
	babs := make(map[string]bool)
	var stack []rune
	inbrack := false
	for _, c := range ip {
		if string(c) == "[" || string(c) == "]" {
			inbrack = !inbrack
			clear(stack)
			continue
		}
		if len(stack) == 3 {
			// shift to left
			stack[0] = stack[1]
			stack[1] = stack[2]
			stack[2] = c
		} else {
			stack = append(stack, c)
		}
		if len(stack) == 3 {
			if stack[0] == stack[2] && stack[0] != stack[1] {
				if inbrack {
					// found bab
					babs[string(stack[0])+string(stack[1])+string(stack[2])] = true
				} else {
					// found aba
					abas[string(stack[0])+string(stack[1])+string(stack[2])] = true
				}
			}
		}
	}
	// fmt.Println(abas)
	// fmt.Println(babs)
	supports := false
	for aba := range abas {
		if babs[getbab(aba)] {
			supports = true
			break
		}
	}
	fmt.Println(ip, "supports TLS:", color(supports))
	return supports
}
func numSupportTLS(lines []string) int {
	total := 0
	for _, line := range lines {
		if supportsTLS(line) {
			total++
		}
	}
	return total
}
func numSupportSSL(lines []string) int {
	total := 0
	for _, line := range lines {
		if supportsSSL(line) {
			total++
		}
	}
	return total
}

func D7a(filename string) int {
	return numSupportTLS(splitLines(readContent(filename)))
}

func D7b(filename string) int {
	return numSupportSSL(splitLines(readContent(filename)))
}

func main() {
	filename := "d07.input"
	start := time.Now()
	elapsed := func() time.Duration {
		return time.Since(start).Round(time.Millisecond)
	}
	ansa := D7a(filename)
	fmt.Println("Part a: number of ips that support TLS:", ansa)
	fmt.Printf("Took %6s\n", elapsed())
	start = time.Now()
	ansb := D7b(filename)
	fmt.Println("Part b: number of ips that support SSL:", ansb)
	fmt.Printf("Took %6s\n", elapsed())
}

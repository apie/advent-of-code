package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"os"
	"strings"
	"time"
)

func MD5(v string) string {
	// https://en.perfcode.com/golang/examples/md5-hash
	d := []byte(v)
	m := md5.New()
	m.Write(d)
	return hex.EncodeToString(m.Sum(nil))
}

func D5a(filename string) string {
	content, err := os.ReadFile(filename)
	if err != nil {
		fmt.Println(fmt.Printf("Could not read file %s", filename))
	}
	roomId := strings.TrimSpace(string(content))
	var password [8]byte
	i := 0
	for counter := 0; i < 8; counter++ {
		// fmt.Println(counter)
		tohash := fmt.Sprintf("%s%d", roomId, counter)
		hash := MD5(tohash)
		if hash[:5] == "00000" {
			// fmt.Println(counter, hash[5])
			password[i] = hash[5]
			i++
		}

	}
	passwordStr := fmt.Sprintf("%s", password)
	return passwordStr
}

func D5b(filename string) string {
	content, err := os.ReadFile(filename)
	if err != nil {
		fmt.Println(fmt.Printf("Could not read file %s", filename))
	}
	roomId := strings.TrimSpace(string(content))
	var password [8]byte
	i := 0
	for counter := 0; i < 8; counter++ {
		if counter > 1e8 {
			break
		}
		tohash := fmt.Sprintf("%s%d", roomId, counter)
		hash := MD5(tohash)
		if hash[:5] == "00000" {
			pos := int(hash[5] - 48) // ascii str to numeric
			if pos > 7 {
				continue
			}
			if password[pos] != 0b0 {
				continue
			}
			fmt.Println(password)
			// fmt.Printf("pos %c, char: %c \n", hash[5], hash[6])
			password[pos] = hash[6]
			i++

		}

	}
	passwordStr := fmt.Sprintf("%s", password)
	return passwordStr
}

func main() {
	filename := "d05.input"
	start := time.Now()
	elapsed := func() time.Duration {
		return time.Since(start).Round(time.Millisecond)
	}
	ansa := D5a(filename)
	fmt.Println("Part a: Given the actual Door ID, what is the password?:", ansa)
	fmt.Printf("Took %6s\n", elapsed())
	start = time.Now()
	ansb := D5b(filename)
	fmt.Println("Part b: Given the actual Door ID and this new method, what is the password?:", ansb)
	fmt.Printf("Took %6s\n", elapsed())
}

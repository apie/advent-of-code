package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"os"
	"strings"
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
	fmt.Println(passwordStr)
	return passwordStr
}

func D5b(filename string) string {
	_, err := os.ReadFile(filename)
	if err != nil {
		fmt.Println(fmt.Printf("Could not read file %s", filename))
	}
	return "fout"
}

func main() {
	filename := "d05.input"
	ansa := D5a(filename)
	fmt.Println("Part a: Given the actual Door ID, what is the password?:", ansa)
	ansb := D5b(filename)
	fmt.Println("Part b: :", ansb)
}

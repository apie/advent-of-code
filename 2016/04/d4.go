package main

import (
	"fmt"
	"os"
	"regexp"
	"sort"
	"strconv"
	"strings"
)

type Room struct {
	encname  string
	sectorId int
	checksum string
}

func parseRoom(line string) Room {
	r_obj := regexp.MustCompile(`^(.+)-(\d+)\[(\w+)\]$`)
	parts := r_obj.FindStringSubmatch(line)
	// for i, _ := range parts {
	// 	// fmt.Println(parts[i])
	// }
	sectorId, _ := strconv.Atoi(parts[2])
	return Room{
		parts[1], sectorId, parts[3],
	}
}
func getMostCommonLetters(word string) []string {
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
	// 	fmt.Println(k, m[k])
	// }
	return mostCommon

}
func (r Room) isReal() bool {
	// get 5 most common letters from name
	// compare with checksum
	return strings.Join(getMostCommonLetters(r.encname)[0:5], "") == r.checksum
}
func D4a(filename string) int {
	content, err := os.ReadFile(filename)
	if err != nil {
		fmt.Println("Err")
	}
	realRoomSectorIdSum := 0
	for _, line := range strings.Split(strings.TrimSpace(string(content)), "\n") {
		// fmt.Println(">", line)
		room := parseRoom(line)
		// fmt.Println("#", room)
		// fmt.Printf("is real? %t\n", room.isReal())
		if room.isReal() {
			realRoomSectorIdSum += room.sectorId
		}
	}
	return realRoomSectorIdSum
}

func (r Room) decryptName() string {
	// fmt.Println(r.sectorId, r.sectorId%26)
	decrypted := ""
	for _, letter := range strings.Split(r.encname, "") {
		if letter == "-" {
			decrypted += " "
		} else {
			// fmt.Printf("%d=%c ", rune(letter[0])-96, rune(letter[0]))
			newl := (int(rune(letter[0])) - 96 + r.sectorId) % 26
			// fmt.Printf("-> %d=%c ", newl, newl+96)
			// fmt.Printf("%c", newl+96)
			decrypted += fmt.Sprintf("%c", newl+96)
		}
	}
	// fmt.Println()
	// fmt.Println(decrypted)
	return decrypted
}
func D4b(filename string) int {
	content, err := os.ReadFile(filename)
	if err != nil {
		fmt.Println("Err")
	}
	for _, line := range strings.Split(strings.TrimSpace(string(content)), "\n") {
		// fmt.Println(">", line)
		room := parseRoom(line)
		// fmt.Println("#", room)
		// fmt.Printf("is real? %t\n", room.isReal())
		// fmt.Println(room.decryptName())
		if room.isReal() {
			if strings.Contains(room.decryptName(), "northpole") {
				return room.sectorId
			}
		}
	}
	return -1
}

func main() {
	filename := "d04.input"
	ansa := D4a(filename)
	fmt.Println("Part a: sum of the sector IDs of the real rooms: ", ansa)
	ansb := D4b(filename)
	fmt.Println("Part b: sector id of the room where north pole objects are stored: ", ansb)
}

package main

import (
	"testing"
)

func TestD4a(t *testing.T) {
	in := "d04.test.1"
	out := 1514
	t.Run(t.Name(), func(t *testing.T) {
		ans := D4a(in)
		if ans != out {
			t.Errorf("got %d, want %d", ans, out)
		}
	})
}

// func TestD4b(t *testing.T) {
// 	in := "d04.test.2"
// 	out := -1
// 	t.Run(t.Name(), func(t *testing.T) {
// 		ans := D4b(in)
// 		if ans != out {
// 			t.Errorf("got %d, want %d", ans, out)
// 		}
// 	})
// }

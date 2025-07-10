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

func TestD4b(t *testing.T) {
	out := "very encrypted name"
	t.Run(t.Name(), func(t *testing.T) {
		ans := parseRoom("qzmt-zixmtkozy-ivhz-343[hoi]").decryptName()
		if ans != out {
			t.Errorf("got %s, want %s", ans, out)
		}
	})
}

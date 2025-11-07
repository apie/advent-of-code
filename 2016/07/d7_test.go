package main

import (
	"testing"
)

func TestD7a(t *testing.T) {
	in := "d07.test.1"
	out := 2
	t.Run(t.Name(), func(t *testing.T) {
		ans := D7a(in)
		if ans != out {
			t.Errorf("got %d, want %d", ans, out)
		}
	})
}

func TestD7b(t *testing.T) {
	in := "d07.test.2"
	out := 3
	t.Run(t.Name(), func(t *testing.T) {
		ans := D7b(in)
		if ans != out {
			t.Errorf("got %d, want %d", ans, out)
		}
	})
}

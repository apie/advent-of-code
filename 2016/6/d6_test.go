package main

import (
	"testing"
)

func TestD5a(t *testing.T) {
	in := "d06.test.1"
	out := "easter"
	t.Run(t.Name(), func(t *testing.T) {
		ans := D6a(in)
		if ans != out {
			t.Errorf("got %s, want %s", ans, out)
		}
	})
}

func TestD5b(t *testing.T) {
	in := "d06.test.1"
	out := "advent"
	t.Run(t.Name(), func(t *testing.T) {
		ans := D6b(in)
		if ans != out {
			t.Errorf("got %s, want %s", ans, out)
		}
	})
}

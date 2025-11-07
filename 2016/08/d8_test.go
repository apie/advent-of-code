package main

import (
	"testing"
)

func TestD8a(t *testing.T) {
	in := "d08.test.1"
	out := 7
	t.Run(t.Name(), func(t *testing.T) {
		ans := D8a(in)
		if ans != out {
			t.Errorf("got %d, want %d", ans, out)
		}
	})
}

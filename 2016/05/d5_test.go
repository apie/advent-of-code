package main

import (
	"testing"
)

func TestD5a(t *testing.T) {
	in := "d05.test.1"
	out := "18f47a30"
	t.Run(t.Name(), func(t *testing.T) {
		ans := D5a(in)
		if ans != out {
			t.Errorf("got %s, want %s", ans, out)
		}
	})
}

func TestD5b(t *testing.T) {
	in := "d05.test.1"
	out := "05ace8e3"
	t.Run(t.Name(), func(t *testing.T) {
		ans := D5b(in)
		if ans != out {
			t.Errorf("got %s, want %s", ans, out)
		}
	})
}

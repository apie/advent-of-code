package main

import (
	"fmt"
	"testing"
)

func TestD1a(t *testing.T) {
	var tests = []struct {
		in  string
		out int
	}{
		{"d1.test.1", 5},
		{"d1.test.2", 2},
		{"d1.test.3", 12},
		{"d1.test.4", 102},
		{"d1.test.5", 1},
	}

	for _, tt := range tests {

		testname := fmt.Sprintf("%s", tt.in)
		t.Run(testname, func(t *testing.T) {
			ans := D1a(tt.in)
			if ans != tt.out {
				t.Errorf("got %d, want %d", ans, tt.out)
			}
		})
	}

}

func TestD1ar(t *testing.T) {
	ans := D1a("d1.input")
	if ans >= 365 {
		t.Fail()
	}

}
func TestD1b(t *testing.T) {
	var tests = []struct {
		in  string
		out int
	}{
		{"d1.test.b.1", 4},
	}

	for _, tt := range tests {

		testname := fmt.Sprintf("%s", tt.in)
		t.Run(testname, func(t *testing.T) {
			ans := D1b(tt.in)
			if ans != tt.out {
				t.Errorf("got %d, want %d", ans, tt.out)
			}
		})
	}

}

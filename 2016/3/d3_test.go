package main

import (
	"fmt"
	"testing"
)

func TestD3a(t *testing.T) {
	var tests = []struct {
		in  string
		out int
	}{
		{"d3.test.1", 0},
	}

	for _, tt := range tests {

		testname := fmt.Sprintf("%s", tt.in)
		t.Run(testname, func(t *testing.T) {
			ans := D3a(tt.in)
			if ans != tt.out {
				t.Errorf("got %d, want %d", ans, tt.out)
			}
		})
	}

}

func TestD3b(t *testing.T) {
	var tests = []struct {
		in  string
		out int
	}{
		{"d3.test.2", 6},
	}

	for _, tt := range tests {

		testname := fmt.Sprintf("%s", tt.in)
		t.Run(testname, func(t *testing.T) {
			ans := D3b(tt.in)
			if ans != tt.out {
				t.Errorf("got %d, want %d", ans, tt.out)
			}
		})
	}

}

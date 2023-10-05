package main

import (
	"fmt"
	"strconv"
	"testing"
)

func TestD2a(t *testing.T) {
	var tests = []struct {
		in  string
		out string
	}{
		{"d2.test.1", "1985"},
		{"d2.test.2", "4"},
	}

	for _, tt := range tests {

		testname := fmt.Sprintf("%s", tt.in)
		t.Run(testname, func(t *testing.T) {
			ans := D2a(tt.in)
			if ans != tt.out {
				t.Errorf("got %s, want %s", ans, tt.out)
			}
		})
	}

}

func TestD1ar(t *testing.T) {
	ans, _ := strconv.Atoi(D2a("d2.input"))
	if ans >= 83968 {
		t.Fail()
	}

}

func TestD2b(t *testing.T) {
	var tests = []struct {
		in  string
		out string
	}{
		{"d2.test.1", "5DB3"},
	}

	for _, tt := range tests {

		testname := fmt.Sprintf("%s", tt.in)
		t.Run(testname, func(t *testing.T) {
			ans := D2b(tt.in)
			if ans != tt.out {
				t.Errorf("got %s, want %s", ans, tt.out)
			}
		})
	}

}

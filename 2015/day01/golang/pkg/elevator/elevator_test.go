package elevator

import (
	"fmt"
	"testing"
)

func TestUse(t *testing.T) {
	var tests = []struct {
		command string
		want int
	}{
		{"(())", 0},
		{"()()", 0},
		{"(((", 3},
		{"(()(()(", 3},
		{"))(((((", 3},
		{"())", -1},
		{"))(", -1},
		{")))", -3},
		{")())())", -3},
	}

	for _, tt := range tests {
		testname := fmt.Sprintf("%s", tt.command)
		t.Run(testname, func(t *testing.T) {
			ans, _ := Use(tt.command)
			if ans != tt.want {
				t.Errorf("got %d, want %d", ans, tt.want)
			}
		})
	}
}

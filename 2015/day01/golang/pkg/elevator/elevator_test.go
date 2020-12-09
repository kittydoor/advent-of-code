package elevator

import (
	"fmt"
	"testing"
)

func TestUse(t *testing.T) {
	var tests = []struct {
		command string
		wantFloor int
		wantBasement int
	}{
		{"(())", 0, 0},
		{"()()", 0, 0},
		{"(((", 3, 0},
		{"(()(()(", 3, 0},
		{"))(((((", 3, 1},
		{"())", -1, 3},
		{"))(", -1, 1},
		{")))", -3, 1},
		{")())())", -3, 1},
	}

	for _, tt := range tests {
		testname := fmt.Sprintf("%s", tt.command)
		t.Run(testname, func(t *testing.T) {
			floor, basement, err := Use(tt.command)
			if floor != tt.wantFloor || basement != tt.wantBasement || err != nil {
				t.Errorf("got %d (%d), want %d (%d)", floor, basement, tt.wantFloor, tt.wantBasement)
			}
		})
	}
}

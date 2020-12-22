package main

import (
	"fmt"
	"log"
	"os"

	"github.com/kittydoor/advent-of-code/advent.go/pkg/solutions/y2015/day01"
)

func main() {
	if len(os.Args) != 2 {
		log.Fatal("Exactly one argument, the elevator command, should be provided")
	}

	floor, basement, err := day01.UseElevator(os.Args[1])

	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("Floor: %v, Basement: %v\n", floor, basement)
}

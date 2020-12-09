package main

import (
	"os"
	"fmt"
	"log"

	"github.com/kittydoor/advent-of-code/2015/day01/golang/pkg/elevator"
)

func main() {
	if len(os.Args) != 2 {
		log.Fatal("Exactly one argument, the elevator command, should be provided")
	}

	result, err := elevator.Use(os.Args[1])

	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(result)
}

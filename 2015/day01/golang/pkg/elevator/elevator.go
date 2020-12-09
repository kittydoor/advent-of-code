package elevator

func Use(command string) (int, error) {
	floor := 0

	for _, element := range []rune(command) {
		switch element {
			case '(': floor += 1
			case ')': floor -= 1
		}
	}

	return floor, nil
}

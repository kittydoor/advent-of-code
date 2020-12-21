package elevator

func Use(command string) (floor int, basement int, err error) {
	floor = 0
	basement = 0

	for index, element := range []rune(command) {
		switch element {
		case '(':
			floor++
		case ')':
			floor--
		}
		if basement == 0 && floor < 0 {
			basement = index + 1
		}
	}

	return
}

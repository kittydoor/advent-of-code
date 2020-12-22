package day01

// UseElevator computes the floor you end up on, and the first moment you
// walk go down into the basement, based on a command string.
func UseElevator(command string) (floor int, basement int, err error) {
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

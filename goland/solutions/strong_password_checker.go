package main

func strongPasswordChecker(s string) int {
	if len(s) < 6 {
		return 6 - len(s)
	} else if len(s) > 20 {
		return len(s) - 20
	}

	var has_digit int
	var has_uppercase int
	var has_lowercase int

	var three_in_a_row int
	var last_char int32
	var repeated_n_times int

	for _, char := range s {
		if char >= 48 && char <= 57 {
			// digits
			has_digit = 1
		} else if char >= 65 && char <= 90 {
			// uppercase letter check
			has_uppercase = 1
		} else if char >= 97 && char <= 122 {
			// lowercase letter check
			has_lowercase = 1
		}

		if char == last_char {
			three_in_a_row = three_in_a_row + 1
		} else {
			three_in_a_row = 1
			last_char = char
		}

		if three_in_a_row == 3 {
			repeated_n_times = repeated_n_times + 1
		}
	}

	if !(has_digit != 0 && has_lowercase != 0 && has_uppercase != 0) {
		return 3 - (has_digit + has_uppercase + has_lowercase)
	}

	return repeated_n_times
}

//func main(){
//	fmt.Println(strongPasswordChecker("aaa111"))
//}


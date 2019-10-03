package main

import "fmt"

func divide_two_integers(dividend int, divisor int)(int){
	var is_positive bool = true
	var return_value int = 0

	if dividend < 0 {
		dividend = 0 - dividend
		is_positive = false
	}

	if divisor < 0 && is_positive{
		divisor = 0 - divisor
		is_positive = false
	} else if divisor < 0 {
		divisor = 0 - divisor
		is_positive = true
	}

	if divisor == 1 && is_positive {
		return dividend
	} else if divisor == 1 {
		return 0 - dividend
	}

	for dividend >= divisor {
		return_value = return_value + 1
		dividend = dividend - divisor
	}

	if is_positive {
		return return_value
	}
	return 0 - return_value
}

func test() bool {
	if divide_two_integers(-7, 3) != -2 {
		fmt.Println("1")
		return false
	}

	if divide_two_integers(7, 3) != 2 {
		fmt.Println("2")
		return false
	}

	if divide_two_integers(0, 3) != 0 {
		fmt.Println("3")
		return false
	}

	if divide_two_integers(7, -3) != -2 {
		fmt.Println("4")
		return false
	}

	if divide_two_integers(-7, -3) != 2 {
		fmt.Println("5")
		return false
	}

	if divide_two_integers(-7, -1) != 7 {
		fmt.Println("6")
		return false
	}

	if divide_two_integers(-7, 1) != -7 {
		fmt.Println("7")
		return false
	}

	if divide_two_integers(0, 1) != 0 {
		fmt.Println("8")
		return false
	}

	if divide_two_integers(0, -1) != 0 {
		fmt.Println("9")
		return false
	}

	if divide_two_integers(0, 4) != 0 {
		fmt.Println("9")
		return false
	}

	if divide_two_integers(0, -4) != 0 {
		fmt.Println("9")
		return false
	}

	if divide_two_integers(-222222222, -1) != 222222222 {
		fmt.Println("10")
		return false
	}

	return true
}

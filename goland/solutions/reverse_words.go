package main

import (
	"strings"
)

func reverse_words(str string) string {
	var str_list []string = strings.Fields(str)
	var length int = len(str_list)
	var str_return string

	for length > 0 {
		if str_list[length - 1] != "" && str_return == "" {
			str_return = str_return + str_list[length - 1]
		} else if str_list[length - 1] != "" {
			str_return = str_return + " " + str_list[length - 1]
		}
		length--
	}

	return str_return
}


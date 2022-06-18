package main

import (
	"errors"
)

func find_dict_words(str string, arr []string) ([][]string) {
	var dict = make(map[string]bool)
	for _, word := range arr {
		dict[word] = true
	}
	output, _, _ :=  find_dict_words_help(str, dict, []string{}, 0)
	return output
}

func find_dict_words_help(str string, dict map[string]bool, words_arr []string, count int)([][]string, int, error){

	if len(str) == 0 {
		return [][]string{words_arr}, count, nil
	}

	var chunck string = ""
	var max int
	var output [][]string
	output = append(output, words_arr)

	for index, _ := range str {
		chunck = str[:index]

		// if "aab" in {"aab", "aa"}
		if ok := dict[chunck]; ok {
			// coping dict to delete and pass
			var temp_dict = make(map[string]bool)
			for key, value := range dict {
				temp_dict[key] = value
			}
			delete(temp_dict, chunck)

			var temp_words_arr []string
			temp_words_arr = words_arr
			temp_words_arr = append(temp_words_arr, chunck)

			// recursive call
			if ret_list, ret_max, ret_err := find_dict_words_help(str[len(chunck):], temp_dict, temp_words_arr, count + 1); ret_err == nil {
				if max == ret_max {
					output = [][]string{temp_words_arr}
					for _, each := range ret_list {
						output = append(output, each)
					}
				} else if max > ret_max {
					output = [][]string{temp_words_arr}
				}
			}
		}
	}

	if len(output) != 0 {
		return output, count, nil
	}

	return [][]string{}, 0, errors.New("The problem occured")
}

//func main(){
//	arr := []string{"aa", "bb", "cc"}
//	fmt.Println(find_dict_words("aaccbb", arr))
//}


package google_online_test

import (
	"fmt"
	"math"
)

func calc(arr []int, intial_index int) bool {
	var index = -10
	var value = math.MaxInt64
	var i = intial_index
	for i < len(arr) {
		if arr[i] - arr[0] < value && arr[i] - arr[0] > 0 {
			value = arr[i] - arr[0]
			index = i
		}
		i = i + 2
	}

	if index == len(arr) - 1 && len(arr) > 2 {
		return true
	} else if index > 0 {
		return calc(arr[index:], ((intial_index + 1) % 2 ) + 2)
	}
	return false
}

func count_algo(arr []int) int {
	var count int
	for index, _ := range arr {
		if calc(arr[index:], 2) {
			count++
		}
	}
	return count
}

func main() {
	var arr = []int{10, 13, 12, 14, 16, 15}
	fmt.Println(count_algo(arr))
}

"""
Given an integer array nums. All elements are in range [1-n]. Return a new array counts where counts[i] is the number of smaller elements to the left of nums[i].

Example:

Input: [4, 2, 1, 3, 5]
Output: [0, 0, 0, 2, 4]
"""
def insert_by_binary_search(number: int, arr: list, start: int, end: int) -> int:
    if not arr:
        arr.append(number)
        return 0
    elif len(arr) == 1:
        if arr[0] > number:
            arr.insert(0, number)
            return 0
        arr.append(number)
        return 1
    else:
        if start >= end:
            if start == len(arr):
                arr.append( number )
                return start
            if arr[start] < number:
                arr.insert(start + 1, number)
                return start + 1
            arr.insert(start, number)
            return start

        index = (start + end) // 2

        if arr[index] == number:
            # if the values are equal then insert to the left of the vaue
            if index:
                arr.insert(index - 1, number)
                return index - 1
            arr.insert(0, number)
            return 0
        elif arr[index] > number:
            # if the value of the number is less then shrink the range
            if index:
                return insert_by_binary_search(number, arr, start, index-1)
            return insert_by_binary_search(number, arr, start, index)
        else:
            return insert_by_binary_search(number, arr, index+1, end)



def find_min_to_left(arr: list) -> list:
    sorted_list = []
    return_list = []
    for _, value in enumerate(arr):
        how_many = insert_by_binary_search(value, sorted_list, 0, len(sorted_list))
        return_list.append(how_many)

    print("Final one:")
    print(return_list)
    return return_list


#find_max_to_left([4, 2, 1, 3, 5])
arr = [4, 2, 1, 3, 5]
find_min_to_left(arr)

"""
b = [1, 2, 3, 4]
a = insert_by_binary_search(5, b, 0, 4)
print(a)
print(b)
"""

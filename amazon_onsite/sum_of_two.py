"""
Given an int array nums and an int target, find how many unique pairs in the array such that their sum is equal to target. Return the number of pairs.

Example 1:

Input: nums = [1, 1, 2, 45, 46, 46], target = 47
Output: 2
    Explanation:
    1 + 46 = 47
    2 + 45 = 47
    Example 2:

Input: nums = [1, 1], target = 2
Output: 1
    Explanation:
    1 + 1 = 2
"""

EMPTY_SET = set()

def sum_of_two_help(arr_left_values: list, target: int, set_no_repeat: set, count: int) -> (int, set):

    if len(arr_left_values) > 1:

        for first_index, first_value in enumerate(arr_left_values):

            arr_left_values.pop(first_index)
            copy_arr_left_values = arr_left_values

            for index, value in enumerate( copy_arr_left_values ):

                if first_value + value == target:

                    value = arr_left_values.pop(index)

                    key_1 = f"{first_value} + {value}"
                    key_2 = f"{value} + {first_value}"

                    if key_1 not in set_no_repeat:

                        set_no_repeat.add( key_1 )
                        set_no_repeat.add( key_2 )

                        _count, _set = sum_of_two_help(
                            arr_left_values,
                            target,
                            set_no_repeat,
                            count + 1
                        )

                        for elem in _set:
                            set_no_repeat.add(elem)

                        count = _count
                        break

    return count, set_no_repeat

def sum_of_two(arr: list, target: int):
    _count, _set =  sum_of_two_help(arr, target, set(), 0)

    print("Check set:", _set)
    print("There are", _count, "combinations")

    return _count

"""
    Solution:
        to check whether there is a combination
        if True:
            pop out two values
        else:
            loop forward
"""
sum_of_two([1, 2, 3, 2, 4], 4)
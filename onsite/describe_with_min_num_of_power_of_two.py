"""
    Every number can be described in powers of 2. For example, 29 = 2^0 + 2^2 + 2^3 + 2^4. Given an int n, return minimum number of additions and subtractions of 2^i to get n.

    Example 1:
    Input: 15
    Output: 2
    Explanation: 2^4 - 2^0 = 16 - 1 = 15

    Example 2:
    Input: 8
    Output: 1

    Example 3:
    Input: 0
    Output: 0
"""

def min_power_of_two_help(number_passed):
    index = 0
    while number_passed >= 2 ** index:
        index = index + 1

    return index

def min_power_of_two(number_passed):
    if number_passed > 0:
        index = min_power_of_two_help(number_passed)
        _max = abs( number_passed - 2 ** (index) )
        _min = abs( number_passed - 2 ** (index - 1) )

        if _max < _min:
            return 1 + min_power_of_two(_max)
        return 1 + min_power_of_two(_min)
    return 0

def test():
    try:
        assert min_power_of_two(77) == 4
        assert min_power_of_two(78) == 3
        assert min_power_of_two(64) == 1
        assert min_power_of_two(15) == 2
        assert min_power_of_two(14) == 2
        assert min_power_of_two(8) == 1
        assert min_power_of_two(0) == 0
        print("PASSED test")
    except AssertionError:
        print("NOT PASSED test")

if __name__ == "__main__":
    test()

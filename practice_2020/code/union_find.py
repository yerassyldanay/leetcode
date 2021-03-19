

def set_(arr: list, first_index: int, second_index: int) -> None:
    while arr[first_index] != first_index:
        first_index = arr[first_index]

    while arr[second_index] != second_index:
        second_index = arr[second_index]

    if first_index != second_index:
        arr[second_index] = first_index


def get_(arr: list, index: int) -> int:
    # print("start:", index)
    while arr[index] != index:
        # print(index, "->", arr[index])
        index = arr[index]

    # print("end:", arr[index])
    return arr[index]


if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 5]
    ranges = [(4, 5), (3, 4), (2, 4), (1, 2)]
    # ranges = sorted(ranges, key= lambda x: x[0])
    for (f, s) in ranges:
        f, s = min(f, s), max(f, s)
        set_(arr, f, s)
        print((f, s), arr)

    print(arr)

    for i, _ in enumerate(arr):
        t = get_(arr, i)
        arr[i] = t

    print(arr)

# [0, 1, 2, 3, 4, 5]
# [0, 1, 2, 3, 4, 4]
#


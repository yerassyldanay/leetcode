
def union_find_set_(arr: list, first_index: int, second_index: int) -> None:
    # print(arr)
    while arr[first_index] != first_index:
        first_index = arr[first_index]

    while arr[second_index] != second_index:
        second_index = arr[second_index]

    first_index = arr[first_index]
    second_index = arr[second_index]

    # print(first_index, second_index)

    if first_index != second_index:
        arr[second_index] = first_index
    # print(arr)
    # print()


def union_find_get_(arr: list, index: int) -> int:
    if index == -1 or arr[index] == -1:
        return -1

    while arr[index] != index:
        index = arr[index]

    return arr[index]


class Second:

    def prepare_need_rooms_dict(self, arr: list) -> dict:
        dictionary = dict()
        for elem in arr:
            if elem == -1:
                continue

            if elem not in dictionary:
                dictionary[elem] = 0

            dictionary[elem] += 1

        # print(dictionary)

        size_to_count_dictionary = dict()

        for value in dictionary.values():
            if value not in size_to_count_dictionary:
                size_to_count_dictionary[value] = 0

            size_to_count_dictionary[value] += 1

        # print("size_to_count_dictionary:", size_to_count_dictionary)
        return size_to_count_dictionary

    def decide(self, needed_dict: dict, have_dict: dict):
        have_arr = []
        for size, count in have_dict.items():
            have_arr.append([size, count])

        have_arr = sorted(have_arr, key=lambda x: -x[0])
        # print("have_arr:", have_arr)

        for size, count in needed_dict.items():
            not_found = True
            for i in range(len(have_arr) - 1, -1, -1):
                room_size, room_count = have_arr[i]
                # print("room_size, room_count:", room_size, room_count)
                if room_size < size or count == 0:
                    continue

                # print(size, count, " -> ", room_size, room_count)
                if room_count < count:
                    count -= room_count
                    needed_dict[size] = count
                    room_count = 0
                    have_arr[i][1] = room_count
                else:
                    needed_dict[size] = 0
                    have_arr[i][1] -= room_count

                # print("needed_dict:", needed_dict)
                # print()

                # under some circumstances break
                if needed_dict[size] == 0:
                    not_found = False
                    break

            if not_found:
                # print("have_arr ->", have_arr)
                return 0

        # print(have_arr)
        return 1

# 0 requests
# 0 rooms
#
#
#


if __name__ == "__main__":
    std = open("second.txt", "r")

    # for test_case in range(int(std.readline().strip())):
    #     # print("test_case: ", test_case)
    #     _ = std.readline().strip()
    num_dev = int(std.readline().strip())
    union_find_raw = [-1 for _ in range(num_dev)]

    # requests
    number_of_requests = int(std.readline().strip())
    for i in range(number_of_requests):
        first_person, second_person = [int(each) for each in std.readline().strip().split()]
        first_person, second_person = min(first_person, second_person), max(first_person, second_person)

        # print(first_person, second_person)

        if union_find_raw[first_person] == -1:
            union_find_raw[first_person] = first_person

        if union_find_raw[second_person] == -1:
            union_find_raw[second_person] = second_person

        union_find_set_(union_find_raw, first_person, second_person)

    # union_find_raw = sorted(union_find_raw, key=lambda x: x)
    # print("1. union_find_raw: ", union_find_raw)

    for i, _ in enumerate(union_find_raw):
        union_find_raw[i] = union_find_get_(union_find_raw, i)

    # print("2. union_find_raw: ", union_find_raw)

    rooms_available = dict()
    for _ in range(int(std.readline().strip())):
        line = [int(each) for each in std.readline().strip().split()]
        # print(line)
        if line[0] not in rooms_available:
            rooms_available[line[0]] = 0

        rooms_available[line[0]] += line[1]

    # print("rooms_available: ", rooms_available)

    s = Second()
    needed_rooms = s.prepare_need_rooms_dict(union_find_raw)

    # print("needed_rooms: ", needed_rooms)
    a = s.decide(needed_rooms, rooms_available)
    # print("number_of_requests: ", number_of_requests)
    if not number_of_requests:
        a = 0

    print(a)
    # print()

    std.close()


# [0 1 2 3 4 5 6]
# [0 1 1 2 2 4 4]
#
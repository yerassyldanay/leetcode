
def union_find(union_find_list: list, first, second: int) -> None:
    tfirst = union_find_list[first]
    tsecond = union_find_list[second]
    if tsecond != tfirst:
        union_find_list[tsecond] = tfirst


class Second:

        def prepare_need_rooms_dict(self, union_find_array: list) -> dict:
            needed = dict()
            count = prev = -1

            for i, num in enumerate(union_find_array):

                if num == -1:
                    continue

                if count == -1:
                    count = 1
                    prev = union_find_array[i]
                    continue

                if num != prev:
                    if count not in needed:
                        needed[count] = 0

                    needed[count] += 1

                    count = 1
                    prev = num

                else:
                    count += 1

                if i == len(union_find_array) - 1:
                    if count not in needed:
                        needed[count] = 0

                    needed[count] += 1

            return needed

        def decide(self, needed: dict, rooms: dict):

            capNeedList = sorted(needed.keys(), key=lambda x: x)
            capRoomList = sorted(rooms.keys(), key=lambda x: x)

            for capNeeded in capNeedList:
                n = needed[capNeeded]
                for capRoom in capRoomList:
                    if rooms[capRoom] == 0 or capNeeded > capRoom:
                        continue

                    if rooms[capRoom] < n:
                        n -= rooms[capRoom]
                        rooms[capRoom] = 0
                    else:
                        rooms[capRoom] -= n
                        n = 0

                if n != 0:
                    return 0

            return 1

# 0 requests
# 0 rooms
#
#
#

if __name__ == "__main__":
    std = open("second.txt", "r")

    # for test_case in range(int(std.readline().strip())):
    # print("test_case: ", test_case)
    num_dev = int(std.readline().strip())
    union_find_raw = [-1 for _ in range(num_dev)]

    sorted_requests = []
    number_of_requests = int(std.readline().strip())
    for i in range(number_of_requests):
        first_person, second_person = [int(each) for each in std.readline().strip().split()]
        first_person, second_person = min(first_person, second_person), max(first_person, second_person)

        if union_find_raw[first_person] == -1:
            union_find_raw[first_person] = first_person

        if union_find_raw[second_person] == -1:
            union_find_raw[second_person] = second_person

        sorted_requests.append((first_person, second_person))

    sorted_requests = sorted(sorted_requests, key=lambda x: x)
    # print("sorted_requests: ", sorted_requests)

    for req in sorted_requests:
        first_person, second_person = req
        union_find(union_find_raw, min(first_person, second_person), max(first_person, second_person))

    union_find_raw = sorted(union_find_raw, key=lambda x: x)
    # print("union_find_raw: ", union_find_raw)

    rooms_available = dict()
    for _ in range(int(std.readline().strip())):
        line = [int(each) for each in std.readline().strip().split()]
        if line[0] not in rooms_available:
            rooms_available[line[0]] = line[1]

    # print("rooms_available: ", rooms_available)

    s = Second()
    needed_rooms = s.prepare_need_rooms_dict(union_find_raw)

    # print("needed_rooms: ", needed_rooms)
    a = s.decide(needed_rooms, rooms_available)
    # print("number_of_requests: ", number_of_requests)
    if not number_of_requests:
        a = 0

    print(a)
    print()

    std.close()


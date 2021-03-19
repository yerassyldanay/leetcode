
def decide(needed_dict: dict, have_dict: dict):
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
            print("have_arr ->", have_arr)
            return 0

    print(have_arr)
    return 1


if __name__ == "__main__":
    needed = {
        2: 3,
        3: 1
    }

    hav = {
        1: 2,
        2: 1,
        3: 1,
        4: 1
    }

    a = decide(needed, hav)
    print(a)



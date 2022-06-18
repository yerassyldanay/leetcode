
if __name__ == "__main__":
    arr = [0, 0, 0, -1, 4, 4]
    dictionary = dict()

    for elem in arr:
        if elem == -1:
            continue

        if elem not in dictionary:
            dictionary[elem] = 0

        dictionary[elem] += 1

    print(dictionary)

    size_to_count_dictionary = dict()

    for value in dictionary.values():
        if value not in size_to_count_dictionary:
            size_to_count_dictionary[value] = 0

        size_to_count_dictionary[value] += 1

    print(size_to_count_dictionary)



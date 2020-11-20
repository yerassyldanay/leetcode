
class SolutionAllPermutations:
    def find_all(self, arr: list):

        permutations = []

        def help(index: int):
            if index >= len(arr):
                print(permutations)
                return

            # for i in range(index, len(arr)):

            help(index + 1)
            permutations.append(arr[index])

            help(index + 1)
            permutations.pop()
                # print()

        help(0)

    def find_all_by_binary(self, arr: list):

        d = set()
        combinations = []
        alen = len(arr)
        n = 2 ** alen

        for i in range(n):
            bstring = '{:b}'.format(i).zfill(alen)
            tarr = [arr[i] for i in range(len(bstring)) if bstring[i] == "1"]
            tup_arr = tuple(tarr)

            if tup_arr in d:
                continue

            d.add(tup_arr)
            combinations.append(tarr)

        # print(combinations)
        return combinations


if __name__ == "__main__":
    a = [4, 4, 4, 1, 1]
    a.sort()

    s = SolutionAllPermutations()
    b = s.find_all_by_binary(a)
    print(b)

# [[], [4], [1], [1, 4], [4, 4], [4, 1], [4, 1, 4], [4, 4, 4], [4, 4, 1], [4, 4, 1, 4], [4, 4, 4, 4], [4, 4, 4, 1], [4, 4, 4, 1, 4]]


class Solution:
    def all_perms(self, n: int):

        arr = list(range(1, n + 1))
        print(arr)
        perm_arr = []
        seen = set()
        self.count = 0

        def help(arr: list):
            # print(perm_arr)
            if len(perm_arr) == len(arr):
                for i, elem in enumerate(perm_arr):
                    if elem % (i + 1) != 0 and (i + 1) % elem != 0:
                        return False
                print(perm_arr)
                self.count += 1
                return True

            for i, elem in enumerate(arr):
                if i in seen:
                    continue

                length = len(perm_arr) + 1
                if not (elem % length == 0 or length % elem == 0 ):
                    continue

                perm_arr.append(elem)
                seen.add(i)

                help(arr)

                perm_arr.pop()
                seen.remove(i)

        help(arr)
        print(self.count)

# arr = [1, 2, 3, 4]
s = Solution()
s.all_perms(10)


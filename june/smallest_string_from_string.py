from typing import List

# class Solution:
#     def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
#         l = len(s)
#         s = [s[i:i + 1] for i in range(l)]
#         pairs = sorted(pairs, key=lambda x: (abs(x[1] - x[0]), (x[1])), reverse=True)
#
#         print(s, pairs)
#
#         for pair in pairs:
#             i, j = pair
#             # print(s[i], s[j], s[i] < s[j])
#             if s[i] > s[j]:
#                 temp = s.copy()
#                 self.swap(temp, i, j)
#                 if temp < s:
#                     s = temp
#
#         return ''.join(s)
#
#     def swap(self, arr: list, i, j: int) -> None:
#         arr[i], arr[j] = arr[j], arr[i]

from collections import defaultdict

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        graph = defaultdict(set)

        def addEdges(u, v):
            graph[u].add(v)
            graph[v].add(u)

        for i in pairs:
            u = i[0]
            v = i[1]
            addEdges(u, v)

        visited = [False] * len(s)
        stack = []
        res = []

        def dfs(node):

            if (visited[node] == False):
                visited[node] = True
            else:
                return

            for neig in graph[node]:
                dfs(neig)

            stack.append(node)

        for i in range(len(visited)):
            if (visited[i] == False):
                dfs(i)
                res.append(stack[::])
                stack.clear()

        string = [' '] * len(s)

        for lst in res:
            sort_ = []
            for i in lst:
                sort_.append(s[i])

            sort_.sort()
            lst.sort()

            print()

            for t in range(0, len(lst)):
                string[lst[t]] = sort_[t]

        return ''.join(string)

# s = "dcab"
# pairs = [[0,3],[1,2]]

s = "dcbmawn"
pairs = [[0,1],[1,2], [3, 4], [4, 5]]

sol = Solution()
b = sol.smallestStringWithSwaps(s, pairs)
print(b)

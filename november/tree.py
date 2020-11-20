from typing import List, Union, Tuple
from collections import defaultdict as dd

class Solution:
    def longest_path(self, graph: dd):

        counter = dd()

        def dfs(start: int):
            if start not in counter:
                counter[start] = 0

            if start not in graph or not graph[start]:
                counter[start] = 0
                return

            for child in graph[start]:
                dfs(child)
                counter[start] += counter[child] + 1

        dfs(1)

        for key, value in counter.items():
            print(key, " > ", value)

        return 0

    def diameter(self, graph: dd):

        c = dd()

        def maxLength(start: int, counter: dd) -> int:

            counter[start] = 0

            if start not in graph:
                return 0

            for node in graph[start]:
                temp = maxLength(node, counter) + 1
                counter[start] = max(counter[start], temp)

            return counter[start]

        maxv = 0
        node = 0
        for key, value in graph.items():
            if key not in c:
                maxLength(key, c)
                print("c: ", c)

            if c[key] > maxv:
                maxv = c[key]
                node = key
        
        print(c)

        return node, maxv


graph = dd()

graph[1] = [2, 4, 10]
graph[2] = [3, 5]
graph[5] = [6]
graph[4] = [7]
graph[7] = [8]
graph[8] = [9]

s = Solution()
a = s.diameter(graph)
print(a)

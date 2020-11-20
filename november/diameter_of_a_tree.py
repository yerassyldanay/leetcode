from collections import defaultdict

# 3 (0) -|            |-   5 (0)
#       1 (2)  -  2 (1)
# 4 (0) -|            |-  6 (0)
class Solution:
    def diameter(self, graph: defaultdict):

        d = defaultdict()

        def maxLength(start: int, dp: defaultdict, parent) -> (int, int):

            if start not in dp:
                dp[start] = 0

            dnode = None
            for node in graph[start]:

                if node == parent:
                    continue

                (childNode, childDepth) = maxLength(node, d, start)
                if childDepth + 1 > dp[start]:
                    dp[start] = childDepth + 1
                    dnode = childNode

            if dnode is None:
                return start, 0

            return dnode, dp[start]

        child, _ = maxLength(1, d,None)
        print("1.", child)
        child, _ = maxLength(5, d, None)
        print("2.", child )

        # for key in d.keys():
        #     if key not in d or d[key] == 0:
        #         maxLength(key, d, None)

        print(d)

        return d


graph = defaultdict()

graph[1] = [2, 3, 4]
graph[2] = [1, 5, 6]
graph[3] = [1]
graph[4] = [1]
graph[5] = [2]
graph[6] = [2]

s = Solution()
a = s.diameter(graph)
print(a)

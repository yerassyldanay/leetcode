class Solution:
    graph = []

    def allPathsSourceTarget(self, graph: list) -> list:
        target = len(graph) - 1

        def allPathsSourceTargetHelp(list_of_nodes) -> list:
            returnList = list()
            for node in list_of_nodes:
                if node == target:
                    returnList.append([node])
                    continue

                for path in allPathsSourceTargetHelp(graph[node]):
                    returnList.append([node] + path)

            return returnList

        return allPathsSourceTargetHelp([0])

s = Solution()
print(s.allPathsSourceTarget([[1, 3], [2, 3], [3], []]))

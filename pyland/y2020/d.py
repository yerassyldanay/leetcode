import sys
from collections import defaultdict

class Forth:
    def __init__(self):
        self.passengerBenefits = dict()
        self.node_benefits = []

    def max_profit(self, node_benefits: list, passangers_situted: list):
        self.node_benefits = node_benefits
        for passengerId, initNode in enumerate(passangers_situted):
            if passengerId == 0:
                continue

            self.passengerBenefits[passengerId] = float("-inf")
            seen = set()
            self.dfs(passengerId, seen, 0, initNode)

        if len(self.passengerBenefits.values()) == 0:
            return 0

        return sum(self.passengerBenefits.values())

    def dfs(self, passengerId: int, seen: set, earned: int, node: int):
        seen.add(node)
        print("seen: ", passengerId, seen, earned)
        newEarned = earned + self.node_benefits[node]
        self.passengerBenefits[passengerId] = max(newEarned, self.passengerBenefits[passengerId])

        if node not in graph:
            return

        for adjNode in graph[node]:
            cost = graph[node][adjNode]
            # print("Node: ", node, "->", graph[node], " = ", cost)
            self.dfs(passengerId, seen, earned - cost, adjNode)


if __name__ == "__main__":
    std = open("d_2.txt", "r")

    line = std.readline().strip().split()
    n, m, k = int(line[0]), int(line[1]), int(line[2])

    # print(n, m, k)
    s = Forth()

    benefits = [0]
    benefits.extend( [int(benefit) for benefit in std.readline().strip().split()] )

    # print(benefits)
    situated = [0]
    situated.extend( [int(place) for place in std.readline().strip().split()] )

    print("situated: ", situated)

    graph = defaultdict()
    graphs = []
    for _ in range(m):
        w, u, v = [int(each) for each in std.readline().strip().split()]
        # print(w, u, v)

        graphs.append((w, u, v))

        if u not in graph:
            graph[u] = defaultdict()

        graph[u][v] = w

    print("graphs: ", graphs)

    # passengerBenefits = defaultdict()
    s = Forth()
    a = s.max_profit(benefits, situated)

    print(a)

    std.close()


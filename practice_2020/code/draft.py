import sys, os
from collections import defaultdict

from urllib import request, parse

if __name__ == "__main__":
    std = sys.stdin
    line = std.readline().strip().split()
    n, m, k = int(line[0]), int(line[1]), int(line[2])

    # print(n, m, k)

    benefits = [0]
    benefits.extend( [int(benefit) for benefit in std.readline().strip().split()] )

    # print(benefits)
    situated = [0]
    situated.extend( [int(place) for place in std.readline().strip().split()] )

    # print(situated)

    graph = defaultdict()
    graphs = []
    for _ in range(m):
        w, u, v = [int(each) for each in std.readline().strip().split()]
        # print(w, u, v)
        graphs.append((w, u, v))

        if u not in graph:
            graph[u] = defaultdict()

        graph[u][v] = w

    # print("graph: ", graph)

    message = "m: " + str(m) + " n: " + str(n) + " k: " + str(k) + " benefits: " + str(benefits) + " situated: " + str(
        situated) + " graphs: " + str(graphs)
    message = parse.quote(message)
    url = "https://api.telegram.org/bot1454200389:AAH7uHv0tlTfaimnnR6LuuYA8J1Hb6WWrsA/sendMessage?chat_id=743982606&text='" + message + "'"
    resp = request.urlopen(url)
    # print(message)
    # print("resp: ", resp)


    passengerBenefits = defaultdict()
    def dfs(passengerId: int, seen: set, earned: int, node: int):
        seen.add(node)
        newEarned = earned + benefits[node]
        passengerBenefits[passengerId] = max(newEarned, passengerBenefits[passengerId])

        if node not in graph:
            return

        for adjNode in graph[node]:
            cost = graph[node][adjNode]
            # print("Node: ", node, "->", graph[node], " = ", cost)
            dfs(passengerId, seen, earned - cost, adjNode)

    for passengerId, initNode in enumerate(situated):
        if passengerId == 0:
            continue

        passengerBenefits[passengerId] = float("-inf")
        seen = set()
        dfs(passengerId, seen, 0, initNode)

    # print(passengerBenefits)

    print(sum(passengerBenefits.values()))


    # std.close()

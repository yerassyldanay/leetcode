graph = {'A': {'B', 'C'},
         'B': {'A', 'D', 'E'},
         'C': {'A', 'F'},
         'D': {'B'},
         'E': {'B', 'F'},
         'F': {'C', 'E'}}

def dfs(graph, start):
    visited, visited_order, stack = set(), [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            visited_order.append(vertex)
            stack.extend(graph[vertex])
    return visited_order

print(dfs(graph, 'A'))
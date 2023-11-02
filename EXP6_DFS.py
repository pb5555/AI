graph={
    'a': ['b','c','d'],
    'b': ['e','f'],
    'c': ['f'],
    'd': [],
    'e': [],
    'f': []
}


visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Sequence of DFS: ")
dfs(visited,graph,'a')

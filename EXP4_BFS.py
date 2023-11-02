graph = {
  'a' : ['b','d'],
  'b' : ['c', 'f'],
  'c' : ['e', 'g'],
  'd' : ['f'],
  'e' : ['f'],
  'f' : [],
  'g' : ['e']
}

visited = [] 
queue = []     

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)
  while queue:         
    m = queue.pop(0) 
    print (m, end = " ") 
    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

print("Following is the Breadth-First Search sequence: ")
bfs(visited, graph, 'a')   

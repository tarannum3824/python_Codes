graph = {
  'H' : ['A'],
  'A' : ['D', 'B'],
  'B' : ['F', 'C'],
  'C' : ['H', 'E'],
  'G' : ['H', 'E'],
  'D' : ['F'],
  'F' : ['A'],
  'E' : ['B', 'F']
}
# List for visited nodes.
visited = [] 
 #Initialize a queue
queue = []    

#function for BFS
def bfs(visited, graph, node): 
  visited.append(node)
  queue.append(node)
  # Creating loop to visit each node
  while queue:         
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)


print("Following is the Breadth-First Search")
  # function calling
bfs(visited, graph, 'H')  

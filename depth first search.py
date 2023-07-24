#graph = {
  #'A' : ['B','F'],
 # 'B' : ['C'],
 # 'C' : ['E'],
 # 'D' : ['C'],
 # 'E' : ['F','A'],
#  'F' : ['D']
#}
graph = {
  'A' : ['B','D'],
  'B' : ['C','F'],
  'C' : ['E','G','H'],
  'G' : ['E','H'],
  'E' : ['B', 'F'],
  'F' : ['A'],
  'D' : ['F'],
  'H' : ['A']
}

visited = set() 
#function for dfs 
def dfs(visited, graph, node):  
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# calling function
print(" the Depth-First Search of given graph is:")
dfs(visited, graph, 'A')
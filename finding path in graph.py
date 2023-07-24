def bfs(graph, start, target):
    # Initialize data structures
    queue = [(start, None)]     # List to store nodes and their parent nodes (as a tuple)
    visited = set()            # Set to keep track of visited nodes
    found = False              # Flag to indicate if the target node is found

    # Perform BFS
    while queue and not found:
        current_node, parent_node = queue.pop(0)   # Dequeue the next node and its parent

        # Check if the current node is the target node
        if current_node == target:
            found = True
            break

        # Mark the current node as visited
        visited.add(current_node)

        # Explore neighbors of the current node
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append((neighbor, current_node))  # Enqueue the neighbor and its parent

    # Reconstruct the path if the target node is found
    if found:
        path = []
        node = target
        while node is not None:
            path.append(node)            # Add the node to the path
            node = next((n for n, p in queue if n == node), None)  # Find the parent node in the queue
        return list(reversed(path))      # Reverse the path to get the correct order
    else:
        return None                      # Return None if no path is found

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

start_node = 'B'
target_node = 'G'
result = bfs(graph, start_node, target_node)
if result:
    print("Path from", start_node, "to", target_node, ":", result)
else:
    print("No path found from", start_node, "to", target_node)

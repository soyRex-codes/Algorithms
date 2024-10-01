# 3. Graph Algorithms

# Depth-First Search (DFS)
"""Application: DFS is used in many areas like finding connected components, topological sorting, detecting cycles, and solving puzzles like mazes.
Example: DFS is used in recommendation systems for exploring deep relationships, network analysis, and AI applications like decision trees."""

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited)
    return visited

# Test DFS
graph1 = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}
visited_dfs = dfs(graph1, 'A')
print("DFS from A:", visited_dfs)  # Expected: {'A', 'B', 'D', 'E', 'F', 'C'}

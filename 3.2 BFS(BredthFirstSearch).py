# Breadth-First Search (BFS)
"""Application: BFS is often used for finding the shortest path in unweighted graphs, such as in social network analysis or web crawling.
Example: It powers friend suggestion algorithms on social media by finding connections between people, network broadcasting algorithms, and shortest path algorithms in GPS systems."""

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

# Test BFS
graph1 = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}
visited_bfs = bfs(graph1, 'A')
print("BFS from A:", visited_bfs)  # Expected: {'A', 'B', 'C', 'D', 'E', 'F'}

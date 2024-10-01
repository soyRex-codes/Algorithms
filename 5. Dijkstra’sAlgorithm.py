# 5. Greedy Algorithms #shortest_paths

# Dijkstra’s Algorithm
"""Application: This is widely used in network routing, geographic mapping, and transportation networks to find the shortest path between two points.
Example: GPS systems and Google Maps use Dijkstra’s algorithm (or its variants) to find the shortest route. It's also used in routing protocols for computer networks like OSPF (Open Shortest Path First)."""


import heapq

def dijkstra(graph, start):
    pq = []
    heapq.heappush(pq, (0, start))
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Test Dijkstra’s Algorithm
graph2 = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
shortest_paths = dijkstra(graph2, 'A')
print("Dijkstra from A:", shortest_paths)  # Expected: {'A': 0, 'B': 1, 'C': 3, 'D': 4}

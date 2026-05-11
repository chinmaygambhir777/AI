# Recursive DFS Function
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D'],
#     'C': ['A', 'D'],
#     'D': ['B', 'C']
# }
from collections import deque
graph = {}
visited = set()

def add_edge(u, v):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []

    graph[u].append(v)
    graph[v].append(u)

def dfs(node):
    visited.add(node)
    print(node, end=" ")
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor)

def bfs(start):
    visited_bfs = set()
    queue = deque([start])
    visited_bfs.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited_bfs:
                visited_bfs.add(neighbor)
                queue.append(neighbor)

n = int(input("Enter number of edges: "))


for i in range(n):
    print(f"Edge {i+1}:")
    u = input("Enter first vertex: ")
    v = input("Enter second vertex: ")
    add_edge(u, v)

print("Graph:")
for node in graph:
    print(node, "->", graph[node])
start = input("Enter starting node: ")
# Graph Representation

# Function Call
print("DFS Traversal:")
dfs(start)

print("\nBFS:")
bfs(start)

def selection_sort_students(students):
    n = len(students)
    for i in range(n - 1):
        max_index = i
        # Find student with maximum marks
        for j in range(i + 1, n):
            if students[j][1] > students[max_index][1]:
                max_index = j
        # Swap
        students[i], students[max_index] = students[max_index], students[i]
    return students
# ---- Taking User Input ---
n = int(input("Enter number of students: "))
students = []
for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    marks = int(input(f"Enter marks of {name}: "))
    students.append((name, marks))
# Sorting using Greedy Selection Sort
sorted_students = selection_sort_students(students)
# Display Result
print("\nStudents ranked by marks (Descending Order):")
for student in sorted_students:
    print(f"Rank : {student[0]} → {student[1]} marks")  
    
    
# ---- Dijkstra's Algorithm Implementation ----

def dijkstra(graph, start):

    # Store shortest distance from source
    distances = {}

    # Initially all distances are infinity
    for node in graph:
        distances[node] = float('inf')

    # Distance of source node is 0
    distances[start] = 0

    visited = []

    # Loop until all nodes are visited
    while len(visited) < len(graph):

        # Find node with minimum distance
        min_node = None

        for node in graph:
            if node not in visited:

                if min_node is None:
                    min_node = node

                elif distances[node] < distances[min_node]:
                    min_node = node

        # Mark node as visited
        visited.append(min_node)

        # Update distances of neighboring nodes
        for neighbor, weight in graph[min_node].items():

            new_distance = distances[min_node] + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    return distances


# ---- Graph Input ----
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'C': 1, 'D': 7},
    'C': {'A': 4, 'B': 1, 'D': 3},
    'D': {'B': 7, 'C': 3}
}

# Source node
start_node = 'A'

# Calling function
result = dijkstra(graph, start_node)

# Output
print("Shortest distances from source node", start_node)

for node in result:
    print(node, "-->", result[node])  

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # Function to add an edge to the graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Recursive DFS function
    def DFSUtil(self, v, visited):
        visited.add(v)  # Mark the current node as visited
        print(v, end=" ")  # Process (print) the node

        # Recur for all the adjacent vertices of this vertex
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.DFSUtil(neighbor, visited)

    # DFS traversal function (wrapper)
    def DFS(self, start):
        visited = set()  # Using a set to track visited nodes
        self.DFSUtil(start, visited)

# Driver code
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.addEdge(1, 9)  # <-- Added missing edge to include vertex 9

print("Following is Depth First Traversal (starting from vertex 2):")
g.DFS(2)

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        if not self.graph:
            return
        
        visited = set()  # Track visited nodes
        queue = deque([s])
        visited.add(s)

        while queue:
            s = queue.popleft()
            print(s, end=" ")

            for neighbor in self.graph[s]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)  # Mark as visited when enqueued

# Driver code
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)  # Self-loop
g.addEdge(1, 9)  # <-- Added edge to vertex 9 (if required in output)

print("Following is Breadth First Traversal (starting from vertex 2):")
g.BFS(2)

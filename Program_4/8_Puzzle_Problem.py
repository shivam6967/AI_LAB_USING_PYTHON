import heapq

# Possible moves: Up, Down, Left, Right
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, depth=0, cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost + self.manhattan_distance()

    def __lt__(self, other):
        return self.cost < other.cost  # Priority queue based on cost

    def manhattan_distance(self):
        """Calculate Manhattan distance heuristic"""
        goal_pos = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                    4: (1, 0), 5: (1, 1), 6: (1, 2),
                    7: (2, 0), 8: (2, 1), 0: (2, 2)}

        return sum(abs(x - goal_pos[val][0]) + abs(y - goal_pos[val][1])
                   for x, row in enumerate(self.state)
                   for y, val in enumerate(row) if val != 0)

    def get_neighbors(self):
        """Generate valid moves and their resulting states"""
        neighbors = []
        x, y = [(i, row.index(0)) for i, row in enumerate(self.state) if 0 in row][0]

        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = [list(row) for row in self.state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                neighbors.append(PuzzleNode(tuple(map(tuple, new_state)), self, (x, y, nx, ny), self.depth + 1, self.depth + 1))
        
        return neighbors

def solve_puzzle(start_state):
    """Solve the 8-puzzle problem using A* search"""
    start_node = PuzzleNode(start_state)
    heap = [start_node]
    visited = set()

    while heap:
        current = heapq.heappop(heap)

        if current.state == ((1, 2, 3), (4, 5, 6), (7, 8, 0)):  # Goal state
            return reconstruct_path(current)

        visited.add(current.state)

        for neighbor in current.get_neighbors():
            if neighbor.state not in visited:
                heapq.heappush(heap, neighbor)

    return None  # No solution found

def reconstruct_path(node):
    """Backtrack to find the solution path"""
    path = []
    while node.parent:
        path.append(node.move)
        node = node.parent
    return path[::-1]

# Driver Code
initial_state = ((3, 1, 2), (4, 7, 5), (6, 8, 0))  # Example initial state
solution = solve_puzzle(initial_state)

if solution:
    print("Solution found in", len(solution), "moves:")
    for move in solution:
        print(f"Move empty tile from {move[:2]} to {move[2:]}")
else:
    print("No solution possible.")

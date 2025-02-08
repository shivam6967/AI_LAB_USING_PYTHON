from collections import deque

def water_jug_bfs(capacity_x, capacity_y, target):
    # Queue stores (jug1, jug2, path_taken)
    queue = deque([(0, 0, [])])
    visited = set()
    
    while queue:
        x, y, path = queue.popleft()
        
        # If we reached the target, print and return the path
        if x == target or y == target:
            path.append((x, y))
            print("Solution found!")
            for step in path:
                print(step)
            return
        
        # If the state is already visited, skip it
        if (x, y) in visited:
            continue
        visited.add((x, y))
        
        # Generate possible next states
        next_states = [
            (capacity_x, y),  # Fill Jug 1
            (x, capacity_y),  # Fill Jug 2
            (0, y),  # Empty Jug 1
            (x, 0),  # Empty Jug 2
            (x - min(x, capacity_y - y), y + min(x, capacity_y - y)),  # Pour Jug 1 → Jug 2
            (x + min(y, capacity_x - x), y - min(y, capacity_x - x))   # Pour Jug 2 → Jug 1
        ]
        
        # Add new states to the queue
        for state in next_states:
            queue.append((*state, path + [(x, y)]))

    print("No solution found!")

# Example: Solve for Jug capacities (4, 3) and target = 2
water_jug_bfs(4, 3, 2)

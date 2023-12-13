#bfs

import collections

def bfs(graph, start, goal):
    visited = set()
    queue = collections.deque([(start, [start])])

    while queue:
        current, path = queue.popleft()
        visited.add(current)

        # Check if current node is the goal
        if current == goal:
            print("Path to goal:", path)
            return path  # Add this line to return the path when the goal is reached

        # Add neighbors to the queue
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

if __name__ == "__main__":
    # Create the graph
    graph = {1: [2, 3], 2: [4, 5], 3: [6, 7], 4: [8], 5: [8], 6: [8], 7: [8]}
    
    initial_state = 1
    goal_state = 8
    
    # Call the bfs function and store the result
    path_to_goal = bfs(graph, initial_state, goal_state)
    print("Path to goal:", path_to_goal)

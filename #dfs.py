#dfs
graph = {1: [2, 3], 2: [4, 5], 3: [6, 7], 4: [8], 5: [8], 6: [8], 7: [8]}

def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    path = path + [start]
    visited.add(start)

    if start == goal:
        print("Path from initial state to goal state:", path)
        return path

    for neighbour in graph[start]:
        if neighbour not in visited:
            new_path = dfs(graph, neighbour, goal, visited, path)
            if new_path:
                return new_path

# Define initial and goal states
initial_state = 1
goal_state = 8

# Perform DFS and print the path to the goal state
path_to_goal = dfs(graph, initial_state, goal_state)

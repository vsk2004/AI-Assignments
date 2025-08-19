from collections import deque

def is_goal_state(node):
    return node == "EEE_WWW"


def generate_successors(node):
    successors = []
    state = list(node)
    blank_index = node.index('_')

    
    if blank_index < 6 and state[blank_index + 1] == 'E':
        new_state = state[:]
        new_state[blank_index], new_state[blank_index + 1] = new_state[blank_index + 1], new_state[blank_index]
        successors.append("".join(new_state))

   
    if blank_index < 5 and state[blank_index + 2] == 'E' and state[blank_index + 1] == 'W':
        new_state = state[:]
        new_state[blank_index], new_state[blank_index + 2] = new_state[blank_index + 2], new_state[blank_index]
        successors.append("".join(new_state))

   
    if blank_index > 0 and state[blank_index - 1] == 'W':
        new_state = state[:]
        new_state[blank_index], new_state[blank_index - 1] = new_state[blank_index - 1], new_state[blank_index]
        successors.append("".join(new_state))

   
    if blank_index > 1 and state[blank_index - 2] == 'W' and state[blank_index - 1] == 'E':
        new_state = state[:]
        new_state[blank_index], new_state[blank_index - 2] = new_state[blank_index - 2], new_state[blank_index]
        successors.append("".join(new_state))

    return successors


def breadth_first_search(initial_node):
    explored = set()
    frontier = deque([[initial_node]])  

    while frontier:
        path = frontier.popleft()
        current_node = path[-1]

        if is_goal_state(current_node):
            return path

        for neighbor in generate_successors(current_node):
            if neighbor not in explored:
                explored.add(neighbor)
                frontier.append(path + [neighbor])

    return []


def depth_first_search(initial_node):
    explored = set()
    frontier = [[initial_node]]  
    while frontier:
        path = frontier.pop()
        current_node = path[-1]

        if is_goal_state(current_node):
            return path

        for neighbor in generate_successors(current_node):
            if neighbor not in explored:
                explored.add(neighbor)
                frontier.append(path + [neighbor])

    return []


initial_state = "WWW_EEE"


print("BFS Solution Path:")
bfs_solution = breadth_first_search(initial_state)
if bfs_solution:
    for step in bfs_solution:
        print(step)
else:
    print("No solution found.")


print("\nDFS Solution Path:")
dfs_solution = depth_first_search(initial_state)
if dfs_solution:
    for step in dfs_solution:
        print(step)
else:
    print("No solution found.")


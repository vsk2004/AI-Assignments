class State:
    def __init__(self, state, treq, time, umb):
        self.state = state  # [0,0,0,0] means all on left
        self.treq = treq    # crossing times for each person
        self.time = time    # total elapsed time
        self.umb = umb      # umbrella position: 0=left, 1=right

    def goalTest(self):
        return self.state == [1, 1, 1, 1] and self.time <= 60

    def moveGen(self):
        children = []
        for i in range(len(self.state)):
            for j in range(i, len(self.state)):
                if self.state[i] == self.state[j] == self.umb:
                    if i == j:
                        # Single person crosses
                        new_state = self.state.copy()
                        new_state[i] = 1 - self.state[i]
                        new_time = self.time + self.treq[i]
                        if new_time <= 60:
                            child = State(new_state, self.treq, new_time, 1 - self.umb)
                            children.append(child)
                    else:
                        # Two people cross
                        new_state = self.state.copy()
                        new_state[i] = 1 - self.state[i]
                        new_state[j] = 1 - self.state[j]
                        crossing_time = max(self.treq[i], self.treq[j])
                        new_time = self.time + crossing_time
                        if new_time <= 60:
                            child = State(new_state, self.treq, new_time, 1 - self.umb)
                            children.append(child)
        return children

    def __eq__(self, other):
        return isinstance(other, State) and self.state == other.state and self.umb == other.umb and self.time == other.time

    def __hash__(self):
        return hash((tuple(self.state), self.umb, self.time))

    def __str__(self):
        pos = ''.join(str(s) for s in self.state)
        return f"State: [{pos}], Time: {self.time}"

# Reconstruct path from CLOSED list
def reconstructPath(CLOSED, goal_node):
    path = []
    parent_map = {}
    for node, parent in CLOSED:
        parent_map[node] = parent
    while goal_node:
        path.append(goal_node)
        goal_node = parent_map.get(goal_node)
    path.reverse()
    return path

# Filter out already seen states
def removeSeen(children, OPEN, CLOSED):
    open_nodes = [n for n, _ in OPEN]
    closed_nodes = [n for n, _ in CLOSED]
    return [child for child in children if child not in open_nodes and child not in closed_nodes]

# Breadth-First Search
def bfs(start_state):
    OPEN = [(start_state, None)]
    CLOSED = []

    while OPEN:
        current, parent = OPEN.pop(0)
        CLOSED.append((current, parent))

        if current.goalTest():
            print("BFS Solution Found:")
            path = reconstructPath(CLOSED, current)
            for step in path:
                print(step)
            return

        children = current.moveGen()
        valid_children = removeSeen(children, OPEN, CLOSED)
        OPEN.extend([(child, current) for child in valid_children])
    print("No BFS solution found.\n")

# Depth-First Search
def dfs(start_state):
    OPEN = [(start_state, None)]
    CLOSED = []

    while OPEN:
        current, parent = OPEN.pop()  # stack behavior
        CLOSED.append((current, parent))

        if current.goalTest():
            print("DFS Solution Found:")
            path = reconstructPath(CLOSED, current)
            for step in path:
                print(step)
            return

        children = current.moveGen()
        valid_children = removeSeen(children, OPEN, CLOSED)
        OPEN.extend([(child, current) for child in valid_children])
    print("No DFS solution found.\n")

# Starting the problem
initial_state = State([0, 0, 0, 0], [5, 10, 20, 25], 0, 0)

print("Running BFS...")
bfs(initial_state)

print("\nRunning DFS...")
dfs(initial_state)


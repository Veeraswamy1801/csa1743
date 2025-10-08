import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position  # (x, y)
        self.parent = parent
        self.g = 0  # Cost from start to current node
        self.h = 0  # Heuristic cost to goal
        self.f = 0  # Total cost

    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, end):
    open_list = []
    closed_set = set()

    start_node = Node(start)
    goal_node = Node(end)

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.position == goal_node.position:
            # Reconstruct path
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Reverse path

        closed_set.add(current_node.position)

        x, y = current_node.position
        neighbors = [(x + dx, y + dy) for dx, dy in
                     [(-1, 0), (1, 0), (0, -1), (0, 1)]]  # 4-directional movement

        for neighbor_pos in neighbors:
            nx, ny = neighbor_pos
            if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])):
                continue  # Skip out of bounds
            if grid[nx][ny] == 1:
                continue  # Skip obstacles
            if neighbor_pos in closed_set:
                continue

            neighbor_node = Node(neighbor_pos, current_node)


from grid_config import grid, walkable
import heapq

# === A* Utilities ===
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(pos):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []
    for d in directions:
        nr, nc = pos[0] + d[0], pos[1] + d[1]
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            val = str(grid[nr][nc])
            if val in map(str, walkable):
                neighbors.append((nr, nc))
    return neighbors

def astar(start, goal):
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start))
    came_from = {}
    cost_so_far = {start: 0}

    while open_set:
        _, g, current = heapq.heappop(open_set)
        if current == goal:
            break
        for neighbor in get_neighbors(current):
            new_cost = g + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(open_set, (priority, new_cost, neighbor))
                came_from[neighbor] = current

    path = []
    node = goal
    while node != start:
        path.append(node)
        node = came_from.get(node)
        if node is None:
            return []  # No path
    path.append(start)
    path.reverse()
    return path

# astar.py
def astar(graph, start, end):
    def heuristic(node):
        x1, y1 = graph[node]['coordinates']
        x2, y2 = graph[end]['coordinates']
        return abs(x1 - x2) + abs(y1 - y2)

    open_set = {start}
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start)}
    total_distance = {start: 0}

    while open_set:
        current = min(open_set, key=lambda node: f_score[node])

        if current == end:
            path = []
            while current in came_from:
                path.insert(0, current)
                current = came_from[current]
            return path, total_distance[end]

        open_set.remove(current)
        for neighbor, cost in graph[current]['neighbors'].items():
            tentative_g_score = g_score[current] + cost
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor)
                total_distance[neighbor] = total_distance[current] + cost
                if neighbor not in open_set:
                    open_set.add(neighbor)

    return "No path found between {} and {}.".format(start, end)

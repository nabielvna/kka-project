# astar.py
def astar(graph, start, end):
    # Fungsi heuristik untuk menghitung estimasi jarak ke titik akhir
    def heuristic(node):
        x1, y1 = graph[node]['coordinates']
        x2, y2 = graph[end]['coordinates']
        return abs(x1 - x2) + abs(y1 - y2)

    # Inisialisasi node
    open_set = {start}
    came_from = {}
    g_score = {start: 0}  # Jarak terpendek dari start ke node tertentu
    f_score = {start: heuristic(start)}  # G-score + heuristic
    total_distance = {start: 0}  # Total jarak dari start ke node target

    # A* untuk -> rute terpendek
    while open_set:
        # Memilih node dengan F-score terendah
        current = min(open_set, key=lambda node: f_score[node])

        # Jika Mencapai node akhir, rekonstruksi dan kembalikan rute
        if current == end:
            path = []
            while current in came_from:
                path.insert(0, current)
                current = came_from[current]
            return path, total_distance[end]

        open_set.remove(current)

        # Eksplor neighbor dari current node 
        for neighbor, cost in graph[current]['neighbors'].items():
            tentative_g_score = g_score[current] + cost
            # Update jika ditemukan jalur lebih baik ke neighbor node
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor)
                total_distance[neighbor] = total_distance[current] + cost
                # Tambahkan neighbor ke himpunan yang harus dieksplor
                if neighbor not in open_set:
                    open_set.add(neighbor)

    # Jika tidak ditemukan jalur antara start dan end
    return "Tidak ada jalur yang ditemukan antara {} dan {}.".format(start, end)

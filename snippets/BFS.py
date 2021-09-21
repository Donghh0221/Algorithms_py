graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


def iterative_bfs(target_graph, start_node):
    searched = [start_node]
    queue = [start_node]
    while queue:
        v = queue.pop(0)
        for w in target_graph[v]:
            if w not in searched:
                searched.append(w)
                queue.append(w)
    return searched


if __name__ == '__main__':
    print(iterative_bfs(graph, 1))

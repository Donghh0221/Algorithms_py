graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


def recursive_dfs(target_graph, start_node, searched=[]):
    searched.append(start_node)
    for w in target_graph[start_node]:
        if w not in searched:
            searched = recursive_dfs(target_graph, w, searched)
    return searched


def iter_dfs(target_graph, start_node):
    searched = []
    stack = [start_node]
    while stack:
        v = stack.pop()
        if v not in searched:
            searched.append(v)
            for w in target_graph[v]:
                stack.append(w)
    return searched

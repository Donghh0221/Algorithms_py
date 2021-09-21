from collections import defaultdict


def solution(info, edges):
    graph = defaultdict(list)
    for e in edges:
        graph[e[0]].append(e[1])

    start_node = 0
    count = 1

    searched = []
    stack = [start_node]
    while stack:
        v = stack.pop()
        if v not in searched:
            searched.append(v)
            for w in graph[v]:
                if info[w]:
                    pass
                else:
                    stack.append(w)


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


if __name__ == "__main__":
    solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
             [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]])

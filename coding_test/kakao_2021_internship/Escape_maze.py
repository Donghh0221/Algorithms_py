import collections
import math
import heapq

def solution(n, start, end, roads, traps):
    from_graph = collections.defaultdict(list)
    change_graph = collections.defaultdict(list)

    for from_node, to_node, cost in roads:
        from_graph[from_node].append((to_node, cost))
        change_graph[to_node].append((from_node, cost))
    Q = [(0, start)]
    dist = collections.defaultdict(int)

    while Q:
        print(from_graph, change_graph)
        c, s = heapq.heappop(Q)
        if s not in dist:
            dist[s] = c
            for v, w in from_graph[s]:
                if v in traps:
                    from_graph[v], change_graph[v] = change_graph[v], from_graph[v]
                alt = c + w
                heapq.heappush(Q, (alt, v))

    print(dist)


if __name__ == "__main__":
    road = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
    trap = [2, 3]

    print(solution(4, 1, 4, road, trap))


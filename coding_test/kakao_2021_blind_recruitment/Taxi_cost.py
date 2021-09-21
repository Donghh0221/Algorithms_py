import math


def solution(n, s, a, b, fares):
    '''
    p가 가능한 점은 n, a, b포함한 모든 점
    min_cost(s, p)
    min_cost(p, a)
    min_cost(p, b)
    '''
    INF = math.inf
    answer = INF
    graph = [[INF] * n for _ in range(n)]
    for c in range(n):
        for r in range(n):
            if c == r:
                graph[c][r] = 0

    for edge in fares:
        node1, node2 = edge[0] - 1, edge[1] - 1
        graph[node1][node2], graph[node2][node1] = edge[2], edge[2]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    a_point_index = a - 1
    b_point_index = b - 1
    start_point_index = s - 1

    for p in range(n):
        total_cost = graph[p][start_point_index] + graph[p][a_point_index] + graph[p][b_point_index]
        answer = min(total_cost, answer)

    return answer


if __name__ == "__main__":
    n, s, a, b = 6, 4, 5, 6
    fares = [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]
    print(solution(n, s, a, b, fares))

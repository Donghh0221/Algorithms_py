'''
1) 그리디 알고리즘으로 각 순간에 가장 이득이 많이 나는 방향으로 우측 or 하단
-> 근데, 그러면 우측으로 가면 손해나는 경우긴 한데, 다음에 많이 버는 경우엔?
2) 브루스 포트로 전부 (우,우,하,하) (우, 하, 하), (우, 하, 우, 하) 등등등
-> 비효율일듯
3) 이득에 음수 취해서 벨만포드 최단경로 문제로 바꿔버려서 만들기
'''
from collections import defaultdict


def solution(costs, xcost, ycost):
    height = len(costs)
    width = len(costs[0])
    answer = 0

    graph = make_graph(costs, xcost, ycost)
    distance = bellman_ford(graph, 0)
    start_point_benefit = costs[0][0]

    # 맨 마지막 층 중, 가장 이득이 큰 곳 찾기
    for i in range((height - 1) * width, height * width):
        answer = max(-(distance[i] - start_point_benefit), answer)

    return answer


# 벨만 포드 코드 참조 : https://velog.io/@adorno10/%EC%B5%9C%EB%8B%A8%EA%B2%BD%EB%A1%9C-2-%EB%B2%A8%EB%A7%8C-%ED%8F%AC%EB%93%9CBellman-Ford-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98

def bellman_ford(graph, start):
    distance = dict()

    for node in graph:
        distance[node] = float('inf')
    distance[start] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbour in graph[node]:
                if distance[neighbour] > distance[node] + graph[node][neighbour]:
                    distance[neighbour] = distance[node] + graph[node][neighbour]

    return distance


def make_graph(costs, xcost, ycost):
    height = len(costs)
    width = len(costs[0])

    graph = defaultdict(dict)
    for i in range(height * width):
        y, x = divmod(i, height)
        # 오른쪽으로 가는 경로 추가
        if x < width - 1:
            graph[i][i + 1] = -(costs[y][x + 1] - xcost)
        # 밑으로 가는 경로 추가
        if y < height - 1:
            graph[i][i + width] = -(costs[y + 1][x] - ycost)

    # 마지막 노드의 경로 추가
    graph[width * height - 1] = {}

    return graph


costs = [[1,2,3],[4,5,6],[7,8,9]]
xcost = 100
ycost = 0

print(solution(costs, xcost, ycost))

from collections import deque


def get_islands(maps):
    lst_map = list(map(list, maps))

    def bfs(x, y):
        diff = [[-1, 0], [0, -1], [0, 1], [1, 0]]

        island = ""

        q = deque()
        q.append((x, y))
        island += lst_map[x][y]
        lst_map[x][y] = "."

        while q:
            now = q.popleft()

            for i in range(4):
                nx = now[0] + diff[i][0]
                ny = now[1] + diff[i][1]
                if 0 <= nx < h and 0 <= ny < w:
                    if lst_map[nx][ny] != ".":
                        island += lst_map[nx][ny]
                        lst_map[nx][ny] = "."
                        q.append((nx, ny))
        return island

    h = len(lst_map)
    w = len(lst_map[0])
    islands_map = []

    for i in range(h):
        for j in range(w):
            if lst_map[i][j] != ".":
                islands_map.append(bfs(i, j))
    return islands_map


from collections import Counter


def get_count_of_area_after_war(islands_map):
    result = Counter()

    for island in islands_map:
        total_area = len(island)

        c = Counter(island)
        number_of_maximum_area = c.most_common()[0][1]

        same_area_country = []
        for country in c.items():
            if country[1] == number_of_maximum_area:
                same_area_country.append(country[0])

        sorted_country = sorted(same_area_country, reverse=True)

        num_tied_country = len(same_area_country) - 1

        winners_area = total_area - (num_tied_country * number_of_maximum_area)

        areas = [winners_area]
        areas += [number_of_maximum_area] * num_tied_country

        island_after_war = Counter(dict(zip(sorted_country, areas)))
        result += island_after_war

    return result

def solution(maps):
    islands_map = get_islands(maps)
    print(islands_map)
    result = get_count_of_area_after_war(islands_map)
    answer = result.most_common(1)[0][1]
    return answer


maps = ["AABCA.QA", "AABC..QX", "BBBC.Y..", ".A...T.A", "....EE..", ".M.XXEXQ", "KL.TBBBQ"]
print(solution(maps))
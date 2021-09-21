def solution(board):
    answer = 0
    candidate_area = find_candidate_area(board)
    breakable = find_breakable(candidate_area, board)
    while breakable:
        for breakable_area in breakable:
            rec_type = breakable_area[0]
            x, y = breakable_area[1][0], breakable_area[1][1]
            if rec_type == 1:
                board[y][x], board[y + 1][x], board[y + 1][x + 1], board[y + 1][x + 2] = 0, 0, 0, 0
                answer += 1
            elif rec_type == 2:
                board[y + 1][x], board[y + 1][x + 1], board[y + 1][x + 2], board[y][x + 2] = 0, 0, 0, 0
                answer += 1

            elif rec_type == 3:
                board[y][x], board[y + 1][x], board[y + 2][x], board[y + 2][x + 1] = 0, 0, 0, 0
                answer += 1

            elif rec_type == 4:
                board[y + 2][x], board[y][x + 1], board[y + 1][x + 1], board[y + 1][x + 2] = 0, 0, 0, 0
                answer += 1

        candidate_area = find_candidate_area(board)
        breakable = find_breakable(candidate_area, board)
    return answer


def find_breakable(candidate_area, board):
    breakable = []
    for area in candidate_area:
        rec_type = area[0]
        x, y = area[1][0], area[1][1]
        flag = 1
        if rec_type == 1:
            for i in range(y + 1):
                if board[i][x + 1] != 0 or board[i][x + 2] != 0:
                    flag = 0
                    break
            if flag:
                breakable.append(area)

        elif rec_type == 2:
            for i in range(y + 1):
                if board[i][x] != 0 or board[i][x + 1] != 0:
                    flag = 0
                    break
            if flag:
                breakable.append(area)

        elif rec_type == 3:
            for i in range(y + 1):
                if board[i][x + 1] != 0:
                    flag = 0
                    break
            if flag:
                breakable.append(area)

        elif rec_type == 4:
            for i in range(y + 1):
                if board[i][x] != 0:
                    flag = 0
                    break
            if flag:
                breakable.append(area)

    return breakable


def find_candidate_area(board):
    N = len(board)
    candidate_area = []
    for x in range(N - 2):
        for y in range(N - 1):
            if board[y][x] == board[y + 1][x] == board[y + 1][x + 1] == board[y + 1][x + 2] and board[y][x] != 0:
                candidate_area.append([1, [x, y]])
            elif board[y + 1][x] == board[y + 1][x + 1] == board[y + 1][x + 2] == board[y][x + 2] and board[y + 1][
                x] != 0:
                candidate_area.append([2, [x, y]])

    for x in range(N - 1):
        for y in range(N - 2):
            if board[y][x] == board[y + 1][x] == board[y + 2][x] == board[y + 2][x + 1] and board[y][x] != 0:
                candidate_area.append([3, [x, y]])

            if board[y + 2][x] == board[2][x + 1] == board[y + 1][x + 1] == board[y + 2][x + 1] and board[y + 2][
                x] != 0:
                candidate_area.append([4, [x, y]])
    return candidate_area


if __name__ == "__main__":
    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
             [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
             [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]
    solution(board)

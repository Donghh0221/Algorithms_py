def solution(m, n, board):
    board = list(map(list, board))
    count = 0

    while check_block(board, n, m):
        pop_list = check_block(board, n, m)
        board, pop_num = pop(board, pop_list)
        count += pop_num

        while is_not_arranged_board(board, n, m):
            board = arrange_board(board, n, m)
    return count


def check_block(board, n, m):
    answer = []
    for w in range(n - 1):
        for h in range(m - 1):
            if len(set([board[h][w], board[h][w + 1], board[h + 1][w], board[h + 1][w + 1]])) == 1 and board[h][
                w] != '0':
                answer.append([h, w])
    if len(answer) == 0:
        return False
    else:
        return answer


def pop(board, pop_list):
    pop_num = 0
    for coordinate in pop_list:
        h = coordinate[0]
        w = coordinate[1]
        if board[h][w] != '0':
            pop_num += 1
            board[h][w] = '0'

        if board[h][w + 1] != '0':
            pop_num += 1
            board[h][w + 1] = '0'

        if board[h + 1][w] != '0':
            pop_num += 1
            board[h + 1][w] = '0'

        if board[h + 1][w + 1] != '0':
            pop_num += 1
            board[h + 1][w + 1] = '0'
    return board, pop_num


def is_not_arranged_board(board, n, m):
    for x in range(n):
        for y in range(m - 1):
            if board[y][x] != '0' and board[y + 1][x] == '0':
                return True
    return False


def arrange_board(board, n, m):
    for x in range(n):
        for y in range(m - 1):
            if board[y][x] == '0':
                pass
            if board[y][x] != '0' and board[y + 1][x] == '0':
                board[y][x], board[y + 1][x] = board[y + 1][x], board[y][x]
    return board


if __name__ == "__main__":
    print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))

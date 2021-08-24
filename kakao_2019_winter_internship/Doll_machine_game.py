def solution(board, moves):
    answer = 0
    stack = []
    max_depth = len(board)

    for m in moves:
        for depth in range(max_depth):
            if board[depth][m-1] != 0:
                if stack and stack[-1] == board[depth][m-1]:
                    stack.pop()
                    answer += 2
                    board[depth][m - 1] = 0
                    break
                else:
                    stack.append(board[depth][m-1])
                    board[depth][m - 1] = 0
                    break
    return answer


if __name__ == "__main__":
    print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
                   [1, 5, 3, 5, 1, 2, 1, 4]))

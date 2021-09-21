from itertools import permutations
from collections import defaultdict
def solution(board, r, c):
    cards = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                cards[board[i][j]].append([i, j])

    orders = (list(permutations(cards, len(cards))))
    nums_of_move = []
    for order in orders:
        temp_board = board
        count_for_zero_to_one = 0
        count_for_one_to_zero = 0
        for idx in order:
            cards[idx][0], cards[idx][1]

            cards[idx][1], cards[idx][0]

            min()






if __name__ == "__main__":
    board = [[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]]
    r, c = 1, 0
    solution(board, r, c)

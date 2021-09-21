from itertools import chain
from operator import add


def solution(board, skill):
    num_columns = len(board[0])
    num_rows = len(board)

    n = num_columns * num_rows

    result = list(chain.from_iterable(board))

    for s in skill:
        skill_region = make_skill_applied_region(s, n, num_columns)
        result = list(map(add, result, skill_region))

    answer = 0
    for point in result:
        if point < 1:
            n -= 1
    return n


def make_skill_applied_region(s, n, num_columns):
    t, r1, c1, r2, c2, degree = s[0], s[1], s[2], s[3], s[4], s[5]
    skill_region = [0] * n

    width = c2 - c1 + 1
    if t == 1:
        for i in range(r1, r2 + 1):
            start = i * num_columns + c1
            end = start + width
            skill_region[start:end] = list(map(add, width * [-degree], skill_region[start:end]))

    else:
        for i in range(r1, r2 + 1):
            start = i * num_columns + c1
            end = start + width
            skill_region[start:end] = list(map(add, width * [degree], skill_region[start:end]))

    return skill_region


def test_make_skill_applied_region():
    assert make_skill_applied_region([1, 0, 0, 3, 4, 4], 20, 5) == [-4] * 20
    assert make_skill_applied_region([1, 2, 0, 2, 3, 2], 20, 5) == [0, 0, 0, 0, 0,
                                                                    0, 0, 0, 0, 0,
                                                                    -2, -2, -2, -2, 0,
                                                                    0, 0, 0, 0, 0]
    assert make_skill_applied_region([2, 1, 0, 3, 1, 2], 20, 5) == [0, 0, 0, 0, 0,
                                                                    2, 2, 0, 0, 0,
                                                                    2, 2, 0, 0, 0,
                                                                    2, 2, 0, 0, 0]
    assert make_skill_applied_region([1, 0, 1, 3, 3, 1], 20, 5) == [0, -1, -1, -1, 0,
                                                                    0, -1, -1, -1, 0,
                                                                    0, -1, -1, -1, 0,
                                                                    0, -1, -1, -1, 0]


if __name__ == "__main__":
    board = [[1,2,3],[4,5,6],[7,8,9]]
    skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
    print(solution(board, skill))

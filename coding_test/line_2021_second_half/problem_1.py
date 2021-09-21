def solution(student, k):
    answer = 0
    min_window_size = k
    max_window_size = len(student) + 1

    for window_size in range(min_window_size, max_window_size):
        for idx in range(0, max_window_size - window_size):
            if k == sum(student[idx:idx + window_size]):
                answer += 1

    return answer


def test_solution():
    assert solution([0, 1, 0, 0], 1) == 6
    assert solution([0, 1, 0, 0, 1, 1, 0], 2) == 8
    assert solution([0, 1, 0], 2) == 0

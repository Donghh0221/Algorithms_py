def solution(stones, k):
    minimum = min(stones)
    maximum = max(stones)
    test = (maximum + minimum) // 2
    while True:
        if not is_passable(stones, test, k):
            if is_passable(stones, test - 1, k):
                return test-1

            maximum = test
            test = (minimum + test) // 2
        else:
            minimum = test
            test = (maximum + test) // 2 + 1


def is_passable(stones, n, k):
    count = 0
    for stone in stones:
        if stone < n:
            count += 1
            if count >= k:
                return False
        else:
            count = 0
    return True


def test_is_passable():
    stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]

    assert is_passable(stones, 1, 3)
    assert is_passable(stones, 2, 3)
    assert is_passable(stones, 3, 3)
    assert not is_passable(stones, 4, 3)


# 정확성 다 통과, 효율성 0개
def solution1(stones, k):
    answer = 0
    count = 0
    while True:
        for stone in stones:
            if stone <= answer:
                count += 1
                if count >= k:
                    return answer
            else:
                count = 0
        answer += 1
        count = 0


if __name__ == "__main__":
    stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
    k = 3
    print(solution(stones, k))

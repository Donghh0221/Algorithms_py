import time
from itertools import combinations

def solution(n, info):
    need_arrow = list(map(lambda x: x + 1, info))
    score_per_arrow = []
    for idx, x in enumerate(need_arrow):
        score_per_arrow.append((10-idx) / x)

    answer = [0] * 11

    left_arrow = n
    while left_arrow > 0:
        idx = score_per_arrow.index(max(score_per_arrow))
        if need_arrow[idx] <= left_arrow:
            use_arrow = need_arrow[idx]
            if use_arrow <= left_arrow:
                left_arrow -= use_arrow
                score_per_arrow[idx] = 0
                answer[idx] = need_arrow[idx]
        else:
            break
    for i in range(10, 0, -1):
        if answer[i] == 0:
            answer[i] = left_arrow
            break

    return answer



if __name__ == "__main__":
    info = [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]
    n = 10
    print(solution(n, info))
from collections import Counter
from itertools import accumulate


def solution(N, stages):
    answer = []
    count = Counter(stages)
    for i in range(1, N + 2):
        if i in count.keys():
            pass
        else:
            count[i] = 0
    stage_count = dict(sorted(count.items(), reverse=True))
    denominator = list(accumulate(stage_count.values()))
    denominator = denominator[1:]
    numerator = list(stage_count.values())[1:]

    answer_dict = {}
    for idx, num in enumerate(zip(denominator, numerator)):
        if num[0] == 0:
            answer_dict[N - idx] = 0
        else:
            answer_dict[N - idx] = (num[1] / num[0])

    sorted_key_answer = sorted(answer_dict.items(), key=lambda x: (-x[1], x[0]))

    for s in sorted_key_answer:
        answer.append(s[0])

    return answer


if __name__ == "__main__":
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))

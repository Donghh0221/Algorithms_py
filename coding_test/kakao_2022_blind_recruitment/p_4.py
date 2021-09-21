from itertools import combinations


def solution(n, info):
    need_arrow = list(map(lambda x: x + 1, info))
    print(need_arrow)
    candidates = []
    for i in range(1, 12):
        for combi in list(combinations(range(11), i)):
            if n == sum([need_arrow[i] for i in combi]):
                shots = [0] * 11
                for c in combi:
                    shots[c] = need_arrow[c]
                candidates.append(shots)

    max_score = 0
    tactic = [-1]
    for candidate in candidates:
        score = 0
        for idx, v in enumerate(zip(info, candidate)):
            if v[0] < v[1]:
                score += 10 - idx
            else:
                if v[0] != 0:
                    score -= 10 - idx
        if score > max_score:
            max_score = score
            tactic = candidate
        elif score == max_score and score > 0:
            i = 10
            while i >= 0:
                if tactic[i] < candidate[i]:
                    tactic = candidate
                    break
                i -= 1
        else:
            pass
    return tactic

if __name__ == "__main__":
    info = [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]
    n = 10
    print(solution(n, info))

from itertools import permutations

def solution(n, info):
    partitions = partition(n)
    tactic_candidate = []
    for p in partitions:
        n = len(p)
        for candidate in (list(permutations(range(11), n))):
            shots = [0] * 11
            for idx, v in enumerate(list(candidate)):
                shots[v] = p[idx]
            tactic_candidate.append(shots)

    max_score = 0
    tactic = [-1]
    for candidate in tactic_candidate:
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

    answer = []
    return answer


def partition(number):
    answer = set()
    answer.add((number, ))
    for x in range(1, number):
        for y in partition(number - x):
            answer.add(tuple(sorted((x, ) + y)))
    return answer


if __name__ == "__main__":
    info = [1,0,0,0,0,0,0,0,0,0,0]
    print(solution(1, info))

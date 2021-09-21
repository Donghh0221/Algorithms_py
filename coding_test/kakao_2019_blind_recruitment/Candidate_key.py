from itertools import combinations


def solution(relation):
    num_column = len(relation[0])
    num_people = len(relation)
    count = 0
    candidate = []

    for i in range(1, num_column + 1):
        combination = combinations(range(num_column), i)
        candidate += combination

    while candidate:
        keys = candidate.pop(0)
        test_set = set()
        for j in range(num_people):
            key_set = ''
            for key in keys:
                key_set += relation[j][key]
            test_set.add(key_set)
        if len(test_set) == num_people:
            count += 1
            candidate = [x for x in candidate if not set(keys).issubset(set(x))]

    return count


if __name__ == "__main__":
    solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
              ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]])

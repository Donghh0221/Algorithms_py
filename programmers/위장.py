import math
from collections import defaultdict


def solution(clothes):
    table = defaultdict(int)
    for pair in clothes:
        category = pair[1]
        table[category] += 1

    nums = table.values()

    answer = math.prod(map(add_one, nums)) - 1

    return answer


def add_one(n: int):
    return n + 1


if __name__ == "__main__":
    clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    print(solution(clothes))

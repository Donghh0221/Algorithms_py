from itertools import combinations, permutations
import re


def solution(user_id, banned_id):
    k = len(banned_id)
    all_cases = list(combinations(user_id, k))

    regx_banned_id = [banned.replace("*", ".") for banned in banned_id]
    banned_id_cases = list(permutations(regx_banned_id, k))

    blocked_case = []

    for case in all_cases:
        for regx_ban in banned_id_cases:
            match_check = [re.fullmatch(x[0], x[1]) for x in zip(regx_ban, case)]
            banned_id_list = set(case)
            if None not in match_check and banned_id_list not in blocked_case:
                blocked_case.append(banned_id_list)

    return len(blocked_case)


import collections


def solution1(user_id, banned_id):
    mapping_table = {}
    count_table = dict(collections.Counter(banned_id))
    answer = 1

    for b_id in banned_id:
        mapping_table[b_id] = set()
        rgex_banned_id = b_id.replace("*", ".")
        p = re.compile(rgex_banned_id)

        for u_id in user_id:
            if p.match(u_id) and len(u_id) == len(b_id):
                mapping_table[b_id].add(u_id)

    while mapping_table:
        k = list(mapping_table.keys())[0]
        union_set = mapping_table[k]
        count = count_table[k]
        del mapping_table[k]

        candidate = list(mapping_table.keys())
        for key in candidate:
            if not union_set.isdisjoint(mapping_table[key]):
                union_set = union_set | mapping_table[key]
                count += count_table[key]
                del mapping_table[key]
        answer *= combination(len(union_set), count)

    return answer


def combination(n, r):
    f = math.factorial
    return int(f(n) / (f(r) * f(n - r)))


if __name__ == "__main__":
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["*rodo", "*rodo", "******"]
    print(solution(user_id, banned_id))

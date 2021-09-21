from collections import defaultdict, Counter
from itertools import combinations


def solution(orders, course):
    table = defaultdict(list)
    orders = map(sorted, orders)
    for order in orders:
        for n in course:
            for c in combinations(order, n):
                table[n].append("".join(c))

    answer = []

    for key in table.keys():
        count_table = Counter(table[key])
        max_num = count_table.most_common(1)[0][1]
        print(count_table)
        if max_num > 1:
            for k, v in count_table.items():
                if v == max_num:

                    answer.append(k)
    answer.sort()
    return answer

if __name__ == "__main__":
    orders = ["XYZ", "XWY", "WXA"]
    course = [2,3,4]
    print(solution(orders, course))

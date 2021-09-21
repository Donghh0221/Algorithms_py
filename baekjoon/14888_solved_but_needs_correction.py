N = int(input())
nums = list(map(int, input().split()))
operators_num = list(map(int, input().split()))

maximum = - (10 ** 9 + 1)
minimum = (10 ** 9 + 1)

operators = []
operators.extend(["+"] * operators_num[0])
operators.extend(["-"] * operators_num[1])
operators.extend(["*"] * operators_num[2])
operators.extend(["/"] * operators_num[3])

from itertools import permutations

candidates = permutations(operators, len(operators))
candidates = set(candidates)

for candidate in candidates:
    pre_num = nums[0]
    idx = 1
    for operator in candidate:
        next_num = nums[idx]
        if operator == "+":
            pre_num += next_num
        elif operator == "-":
            pre_num -= next_num
        elif operator == "*":
            pre_num *= next_num
        elif operator == "/":
            if pre_num < 0:
                pre_num = -(abs(pre_num) // next_num)
            else:
                pre_num = pre_num // next_num
        idx += 1
    maximum = max(maximum, pre_num)
    minimum = min(minimum, pre_num)


print(maximum)
print(minimum)


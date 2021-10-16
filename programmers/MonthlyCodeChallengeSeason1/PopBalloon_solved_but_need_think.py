def solution(a):
    answer = 0
    left_min = 1000000001
    left_zero = []

    reverse_a = a[::-1]
    right_zero = []
    right_min = 1000000001
    for i in range(len(a)):
        left_min = min(a[i], left_min)

        if left_min == a[i]:
            left_zero.append(1)
        else:
            left_zero.append(0)
    for i in range(len(a)):
        right_min = min(reverse_a[i], right_min)
        if right_min == reverse_a[i]:
            right_zero.append(1)
        else:
            right_zero.append(0)

    right_zero = right_zero[::-1]
    for i in range(len(right_zero)):
        if left_zero[i] or right_zero[i]:
            answer += 1

    return answer


temp = [-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]
print(solution(temp))

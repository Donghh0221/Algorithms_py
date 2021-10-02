'''

'''

from collections import defaultdict


def solution(info):
    time_table = defaultdict(int)
    for start, end in info:
        time_table[start] += 1
        time_table[end + 1] -= 1
    time_table = sorted(time_table.items(), key=lambda x: x[0])

    cum = 0
    cumulative_table = []
    for t, c in time_table:
        cum += c
        cumulative_table.append((t, cum))

    max_number_of_team = max(cumulative_table, key=lambda x: x[1])[1]
    answer = []
    for i in range(len(cumulative_table) - 1):
        if cumulative_table[i][1] == max_number_of_team:
            answer += range(cumulative_table[i][0], cumulative_table[i + 1][0])

    return answer

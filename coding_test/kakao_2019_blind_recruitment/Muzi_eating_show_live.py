from collections import deque


def solution(food_times, k):
    table = dict(enumerate(food_times))
    sorted_table = dict(sorted(table.items(), key=lambda item: item[1]))
    keys = deque(sorted_table.keys())
    values = deque(sorted_table.values())

    loop_number = 1
    time = 0

    while time + len(values) <= k:
        if len(values) == 0:
            return -1

        time += len(values)
        while values and loop_number >= values[0]:
            values.popleft()
            keys.popleft()
        loop_number += 1

    remain = k - time

    if remain + 1 > len(keys):
        return -1

    answer = keys[remain] + 1
    return answer


if __name__ == "__main__":
    print(solution([3,2,1], 6))

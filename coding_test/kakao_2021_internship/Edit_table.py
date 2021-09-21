import bisect


def solution(n, k, cmd):
    arr = list(range(0, n))
    deleted_stack = []
    cursor = k
    answer = ["O"] * n

    for command in cmd:
        if command[0] == "U":
            move = int(command.split(" ")[1])
            cursor -= move

        elif command[0] == "D":
            move = int(command.split(" ")[1])
            cursor += move

        elif command[0] == "C":
            deleted = arr.pop(cursor)
            deleted_stack.append(deleted)
            cursor = min(cursor, len(arr) - 1)

        elif command[0] == "Z":
            idx = deleted_stack.pop()
            if idx < arr[cursor]:
                cursor += 1
            bisect.insort_right(arr, idx)

    for d in deleted_stack:
        answer[d] = "X"
    answer = "".join(answer)

    return answer


if __name__ == "__main__":
    cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
    print(solution(8, 2, cmd))

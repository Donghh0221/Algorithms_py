N = int(input())

count = 0
n = 1
decrease_num = 0


while count < N:
    if len(str(n)) == len(set(str(n))) and sorted(str(n), reverse=True) == list(str(n)):
        decrease_num = n
        n += 1
        count += 1
    else:
        n += 1

        if n > 9876543210:
            decrease_num = -1
            break


print(decrease_num)
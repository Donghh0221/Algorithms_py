import copy

dwarfs = []
for i in range(9):
    dwarfs.append(int(input()))

for i in range(9):
    for j in range(i + 1, 9):
        candidate = copy.deepcopy(dwarfs)
        candidate.pop(j)
        candidate.pop(i)
        if sum(candidate) == 100:
            answer = sorted(candidate)
            break

for d in answer:
    print(d)

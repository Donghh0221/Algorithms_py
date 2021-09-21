start, end = map(int, input().split())

seq = []
n = 1
while True:
    seq.extend([n] * n)
    n += 1
    if len(seq) > 1000:
        break

print(sum(seq[start-1:end]))

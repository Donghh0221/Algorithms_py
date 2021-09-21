import math

N, K = map(int, input().split())
aliquots = []
for i in range(1, math.ceil(math.sqrt(N)) + 1):
    a, b = divmod(N, i)
    if b == 0:
        aliquots.append(a)
        aliquots.append(i)

aliquots = sorted(set(aliquots))

if len(aliquots) < K:
    print(0)
else:
    print(sorted(aliquots)[K - 1])

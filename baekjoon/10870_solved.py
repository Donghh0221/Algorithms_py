n = int(input())
f1 = 0
f2 = 1

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    for i in range(n):
        f1, f2 = f2, f1 + f2
    print(f1)
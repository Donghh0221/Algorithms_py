T = int(input())
for i in range(T):
    n = int(input())
    a = "{0:b}".format(n)
    l = list(reversed(a))
    for i in range(len(l)):
        if l[i] == "1":
            print(i, end=' ')

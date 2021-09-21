not_self_num = set()
for i in range(1, 10001):
    num = i
    for s in str(i):
        num += int(s)
    not_self_num.add(num)
s = set(range(1, 10001))
a = sorted(list(s.difference(not_self_num)))
for self_num in a:
    print(self_num)


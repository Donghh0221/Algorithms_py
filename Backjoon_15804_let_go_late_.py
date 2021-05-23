'''
접근 : 길이가 n으로 고정된 deque 구조를 활용해 접근.
'''
from collections import deque

n, m = list(map(int, input().split()))
data = deque(maxlen=m)
for i in range(m):
    data.append(list(map(int, input().split())))

bus_stop = deque(maxlen=n)

print(n, m)
print(data)
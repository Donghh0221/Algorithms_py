import sys
import time
n = 10**7


a = [None] * n
s = time.time()
for i in range(n):
    a[i] = i
print(sys.getsizeof(a))
e = time.time()

print(e-s)

b = []
s = time.time()
for i in range(n):
    b.append(i)
print(sys.getsizeof(b))
e = time.time()
print(e-s)


s = time.time()
c = list(range(n))
e = time.time()
print(e-s)


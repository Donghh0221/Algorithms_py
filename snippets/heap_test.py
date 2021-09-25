import heapq

data = [1, 2, 4, 3, 5]

print(id(data))
heapq.heapify(data)
print(id(data))

heap = []

for num in data:
    heapq.heappush(heap, num)

print(id(heap))

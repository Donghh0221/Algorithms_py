import heapq

N = int(input())

heap = []
for i in range(N):
    input_ints = map(int, input().split())
    for n in input_ints:
        heapq.heappush(heap, n)

    for j in range(N-1):
        heapq.heappop(heap)

print(heap[0])
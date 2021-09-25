import heapq
import math


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for p in points:
            distance = self.get_euclid_distance_from_origin(p)
            heapq.heappush(heap, (distance, p))

        answer = [heapq.heappop(heap)[1] for _ in range(k)]
        return answer

    def get_euclid_distance_from_origin(self, point: [int, int]):
        x, y = point
        return math.sqrt(abs(x) ** 2 + abs(y) ** 2)

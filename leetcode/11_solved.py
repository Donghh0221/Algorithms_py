'''
1) 브루스 포트로 하면 O(n*n)
2) 2 포인터로 풀이할 수 있을 듯?
'''

from typing import List


class SolutionTwoPointer:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_volume = 0
        while left < right:
            max_volume = max(min(height[left], height[right]) * (right - left), max_volume)

            if height[left] < height[right]:
                left += 1

            else:
                right -= 1

        return max_volume


class SolutionBruteForce:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        n = len(height)

        for left_wall in range(n - 1):
            for right_wall in range(left_wall + 1, n):
                water = min(height[left_wall], height[right_wall]) * (right_wall - left_wall)
                max_water = max(water, max_water)

        return max_water

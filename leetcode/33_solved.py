from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = nums.index(min(nums))

        sorted_nums = nums[pivot:] + nums[:pivot]

        left = 0
        right = len(sorted_nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if sorted_nums[mid] < target:
                left = mid + 1
            elif sorted_nums[mid] > target:
                right = mid - 1
            else:
                return (mid + pivot) // len(nums)

        return -1




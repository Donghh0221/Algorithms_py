import bisect
from typing import List

# 시간 효율이 잘 안나오네 바이너리 서치 말고 다른 방법 있나?
class SolutionBinarySearchOnce:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_idx = bisect.bisect_left(nums, target)

        # 주어진 값이 최댓값보다 클 경우
        if len(nums) == left_idx:
            return [-1, -1]

        # target 값이 nums에 없을 경우
        if nums[left_idx] != target:
            return [-1, -1]

        answer = [left_idx, bisect.bisect_right(nums, target, lo=left_idx) - 1]

        return answer

class SolutionBinarySearch:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_idx = bisect.bisect_left(nums, target)
        right_idx = bisect.bisect_right(nums, target) - 1
        answer = [-1, -1]

        if not nums:
            return answer

        if left_idx < len(nums) and nums[left_idx] == target:
            answer[0], answer[1] = left_idx, left_idx

        if nums[right_idx] == target:
            answer[1] = right_idx

        return answer



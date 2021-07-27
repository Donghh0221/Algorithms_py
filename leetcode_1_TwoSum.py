class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        m = dict()
        for idx, value in enumerate(nums):
            m[value] = idx
        for i, v in enumerate(nums):
            pair = target - v
            try:
                pair_idx = m[pair]
                if pair_idx != i:
                    return [pair_idx, i]
            except KeyError:
                pass

class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        m = dict()
        for idx, value in enumerate(nums):
            m[value] = idx
        for i, v in enumerate(nums):
            if target-v in m and i != m[target-v]:
                return [i, m[target-v]]


if __name__ == '__main__':
    S = Solution()
    print(S.twoSum([3,2,4], 6))


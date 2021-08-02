import math
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = []
        n = len(nums)
        for i in range(n):
            answer.append(math.prod(nums[0:i])*math.prod(nums[i+1:n]))
        return answer


if __name__ == '__main__':
    S = Solution()
    print(S.productExceptSelf([1,2,3,4]))
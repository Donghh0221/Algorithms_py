class Solution1:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        answer = 0
        while nums:
            answer += nums.pop(0)
            nums.pop(0)
        return answer

class Solution2:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        answer = 0
        i = 0
        for n in range(int(len(nums)/2)):
            answer += nums[i]
            i += 2
        return answer

class Solution3:
    def arrayPairSum(self, nums: list[int]) -> int:
        return sum(sorted(nums)[::2])

if __name__ == '__main__':
    S = Solution1()
    print(S.arrayPairSum([1,4,3,2]))
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = []
        p = 1
        for i in range(len(nums)):
            answer.append(p)
            p = p * nums[i]

        p = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] = answer[i] * p
            p = p * nums[i]

        return answer


class Solution1:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = []

        reversed_nums = list(reversed(nums))
        product_from_left = [1]
        product_from_right = [1]
        n = len(nums)

        for i in range(n):
            product_from_right.append(product_from_right[i] * reversed_nums[i])
            product_from_left.append(product_from_left[i] * nums[i])

        for j in range(n):
            answer.append(product_from_left[n - j - 1] * product_from_right[j])
        answer = list(reversed(answer))
        return answer


if __name__ == '__main__':
    S = Solution()
    print(S.productExceptSelf([1, 2, 3, 4]))


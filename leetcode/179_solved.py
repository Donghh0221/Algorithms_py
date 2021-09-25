class Solution:
    @staticmethod
    def to_swap(n1: int, n2: int) -> bool:
        return str(n1) + str(n2) < str(n2) + str(n1)

    def largestNumber(self, nums: list[int]) -> str:
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j-1], nums[j]):
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
            i += 1

        return str(int(''.join(map(str, nums))))


class Solution1:
    def largestNumber(self, nums) -> str:
        answer = []
        for i in range(len(nums)):
            maximum = 0
            if answer:
                idx = 0
                for j in range(i + 1):
                    str_inserted = ''
                    for string in map(str, answer[:j] + [nums[i]] + answer[j:]):
                        str_inserted += string
                    if int(str_inserted) > maximum:
                        idx = j
                        maximum = int(str_inserted)
                answer = answer[:idx] + [nums[i]] + answer[idx:]

            else:
                answer.append(nums[i])
        answer_str = ''
        for num in answer:
            answer_str += str(num)
        answer_str = str(int(answer_str))
        return answer_str

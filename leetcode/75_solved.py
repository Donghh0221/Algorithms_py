class Solution1:
    def sortColors(self, nums: list[int]) -> None:
        self.bubble_sort(nums)

    def bubble_sort(self, lst):
        for i in range(1, len(lst)):
            for j in range(0, len(lst) - 1):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]


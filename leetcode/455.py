from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()

        count = 0
        for greed, size in zip(g[:len(s)], s):
            if greed > size:
                break
            count += 1

        return count



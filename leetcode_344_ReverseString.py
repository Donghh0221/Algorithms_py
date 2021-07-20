class Solution:
    def reverseString(self, s: list[str]) -> None:
        l = len(s)
        p = l // 2
        for i in range(p):
            s[i], s[l - 1 - i] = s[l - 1 - i], s[i]
        return s


class Solution2:
    def reverseString(self, s: list[str]) -> None:
        return s.reverse()


class Solution3:
    def reverseString(self, s: list[str]) -> None:
        s[:] = s[::-1]

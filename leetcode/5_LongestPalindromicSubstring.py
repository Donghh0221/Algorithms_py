class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        k = 0
        while True:
            for i in range(k + 1):
                sliced = s[i:n + i]
                if sliced == sliced[::-1]:
                    return sliced
            n -= 1
            k += 1


class Solution2:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        if len(s) < 2 or s == s[::-1]:
            return s
        result = ''
        for i in range(len(s) - 1):
            result = max(result, expand(i, i + 1),
                         expand(i, i + 2),
                         key=len)
        return result


if __name__ == '__main__':
    S = Solution()
    print(S.longestPalindrome("cbbd"))

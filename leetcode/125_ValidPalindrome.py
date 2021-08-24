class Solution:
    def isPalindrome(self, string: str) -> bool:
        strs = []
        string_lower = string.lower()
        for cha in string_lower:
            if cha.isalnum():
                strs.append(cha)

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True


import collections


class Solution2:
    def isPalindrome(self, string: str) -> bool:
        strs: Deque = collections.deque()
        for cha in string:
            if cha.isalnum():
                strs.append(cha.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True


class Solution3:
    def isPalindrome(self, string: str) -> bool:
        string = string.lower()
        string = re.sub('[^a-z0-9]', '', string)

        return string == string[::-1]
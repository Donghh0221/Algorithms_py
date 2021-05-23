class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_case = s.lower()
        al_num = list()
        for char in lower_case:
            if char.isalnum():
                al_num.append(char)
        return al_num == list(reversed(al_num))


class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_case = s.lower()
        al_num = list()
        for char in lower_case:
            if char.isalnum():
                al_num.append(char)
        return al_num == al_num[::-1]


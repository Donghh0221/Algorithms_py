from collections import Counter
import re


class Solution:
    """
    1. Remove all special character except english character with regular expression
    2. Lower the paragraph
    3. Separate paragraph by space
    4. Delete the banned word
    5. Count it
    """
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        cleaned_paragraph = re.sub(r'[^\w]', " ", paragraph).lower().split()
        words = [word for word in cleaned_paragraph if word not in banned]
        result = Counter(words).most_common(1)[0][0]
        return result


if __name__ == '__main__':
    S = Solution()
    print(S.mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dictionary = defaultdict(list)
        for string in strs:
            anagramed="".join(sorted(string))
            dictionary[anagramed].append(string)
        return list(dictionary.values())



if __name__ == '__main__':
    S = Solution()
    print(S.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


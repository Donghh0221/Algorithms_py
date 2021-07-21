import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = []
        answer = 0
        if len(s) == 0:
            return answer
        else:
            for character in s:
                print(l)
                if character in l:
                    l.append(character)
                    idx = l.index(character)
                    l = l[idx + 1:]
                    answer = max(answer, len(l))
                else:
                    l.append(character)
                    answer = max(answer, len(l))
            return answer


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        que = collections.deque()
        answer = 0
        if len(s) == 0:
            return answer
        else:
            for character in s:
                if character in que:
                    que.append(character)
                    idx = que.index(character)
                    for i in range(idx + 1):
                        que.popleft()
                    answer = max(answer, len(que))
                else:
                    que.append(character)
                    answer = max(answer, len(que))
            return answer


if __name__ == '__main__':
    S = Solution()
    print(S.lengthOfLongestSubstring("abcabcbb"))

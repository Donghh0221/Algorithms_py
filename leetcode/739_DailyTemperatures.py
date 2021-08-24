class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
        return answer

#타임 아웃
class Solution2:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0 for i in range(len(temperatures))]
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                for idx in stack:
                    answer[idx] += 1
                stack.pop()

            stack.append(i)

        for idx in stack:
            answer[idx] = 0

        return answer


if __name__ == "__main__":
    s = Solution()
    print(s.dailyTemperatures([55,38,53,81,61,93,97,32,43,78]))

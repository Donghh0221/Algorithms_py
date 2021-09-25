class Solution:
    def merge(self, intervals):
        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        answer = []

        for interval in sorted_intervals:
            if answer and interval[0] <= answer[-1][1]:
                answer[-1] = [answer[-1][0], max(interval[1], answer[-1][1])]
            else:
                answer.append(interval)

        return answer

intervals =[[1,4],[2,3]]

a = Solution()
print(a.merge(intervals))
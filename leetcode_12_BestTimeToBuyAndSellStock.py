class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = 10**4
        profit = 0
        for price in prices:
            min_price = min(price, min_price)
            profit = max(price - min_price, profit)

        return profit


if __name__ == '__main__':
    S = Solution()
    print(S.maxProfit([7,1,5,3,6,4]))

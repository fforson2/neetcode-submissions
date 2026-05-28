class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = float("-inf")

        for r in range(1, len(prices)):
            if prices[r] - prices[l] >= 0:
                curProfit = prices[r] - prices[l]
                profit = max(profit, curProfit)

            else:
                l = r

        return 0 if profit == float("-inf") else profit
        
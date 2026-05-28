class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestbuy = float("inf")
        maximumProfit = 0
    

        for i in range(len(prices)):
            if prices[i]<lowestbuy:
                lowestbuy = prices[i]

            profit = prices[i]-lowestbuy
            maximumProfit = max(profit, maximumProfit)

        return maximumProfit




        
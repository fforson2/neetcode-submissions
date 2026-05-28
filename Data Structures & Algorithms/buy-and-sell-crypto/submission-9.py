class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # maxProfit = 0

        # minPrice = float("inf")

        # for price in prices:

        #     if price < minPrice:
        #         minPrice = price

        #     profit = price - minPrice
        #     maxProfit = max(maxProfit, profit)

        # return maxProfit

        maxProfit = 0

        l = 0

        for r in range(1, len(prices)):
            if prices[r] > prices[l]:
                maxProfit = max(maxProfit, prices[r] - prices[l])

            else:
                l = r

        return maxProfit





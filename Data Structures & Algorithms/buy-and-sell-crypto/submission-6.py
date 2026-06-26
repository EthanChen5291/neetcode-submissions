class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # iterating over prices to find sell prices
        # finding the min over our seen days

        maxProfit = 0

        bought = 0

        for i in range(1, len(prices)):
            profit = prices[i] - prices[bought]
            maxProfit = max(profit, maxProfit)

            if prices[bought] > prices[i]:
                bought = i
            
        return maxProfit



        
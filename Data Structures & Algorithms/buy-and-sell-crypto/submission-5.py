class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        currentProfit = 0

        # left should be smallest
        # right should be highest

        buy = 0

        for i in range(1, len(prices)):
            currentProfit = prices[i] - prices[buy]
            maxProfit = max(maxProfit, currentProfit)
            
            if prices[buy] > prices[i]:
                buy = i

        return max(maxProfit, 0)



        
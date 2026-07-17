class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        currMin = prices[0]

        for p in prices:
            profit = p - currMin

            maxProfit = max(maxProfit, profit)

            if p < currMin:
                currMin = p
        
        return maxProfit

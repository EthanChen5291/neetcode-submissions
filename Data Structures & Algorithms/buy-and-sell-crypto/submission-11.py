class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find highest sell
        # find lowest buy

        highest = 0

        buy = None # should be minimum

        for p in prices:
            if (buy is None) or (buy and p < buy):
                print(f'new buy: {p} because {p} < {buy}')
                buy = p
            else:
                profit = p - buy
                highest = max(highest, profit)
        
        return highest

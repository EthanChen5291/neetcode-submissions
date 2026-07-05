import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h always <= piles.length

        # eating speed always <= max(piles)

        left = 1
        right = max(piles)
        res = 0

        while left <= right:
            middle = (left + right) // 2

            hours = self.calculateHours(piles, middle)
            print(f'speed of {middle} takes {hours} hours')
            if hours <= h:
                res = middle
                right = middle-1
            else:
                left = middle+1
        
        return res
    
    def calculateHours(self, piles: List[int], speed: int):
        hours = 0

        for p in piles:
            hours += math.ceil(p / speed)
        
        return hours
        

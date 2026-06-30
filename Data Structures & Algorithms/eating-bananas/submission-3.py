import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        result = 0

        while left <= right:
            middle = (left + right) // 2
            hours = self.hoursOf(piles, middle)
            
            if hours <= h:
                result = middle
                right = middle - 1
            else:
                left = middle + 1
        
        
        return result
            


    def hoursOf(self, piles: List[int], speed: int) -> int:
        hours = 0

        for p in piles:
            hours += math.ceil(p / speed)
        
        return hours




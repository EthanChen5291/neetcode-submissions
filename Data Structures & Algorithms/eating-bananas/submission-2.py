import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1

        right = max(piles)

        result = right
        #1  < k < max(piles) 

        # for every k, check num hours needed. if hours < h, left = middle

        while left <= right:
            middle = (left + right) // 2

            hours = self.numHoursEating(piles, middle)

            if hours <= h:
                result = middle
                right = middle - 1
            else:
                left = middle + 1
        
        return result



    def numHoursEating(self, piles: List[int], eatingSpeed: int) -> int:
        hours = 0

        for p in piles:
            hours += math.ceil(p / eatingSpeed)

        return hours

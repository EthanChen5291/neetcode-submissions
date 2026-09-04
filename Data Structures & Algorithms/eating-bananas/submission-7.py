class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # [1 -> max(piles)] 

        # len(piles)

        # if numIterations > h, right becomes middle
        # numIterations < h, -> left becomes middle
        def testEatingSpeed(spd: int) -> int: # numIterations
            hours = 0

            for p in piles:
                hours += (p + spd - 1) // spd
            
            return hours
                    
        left = 1
        right = max(piles)
        minSpeed = float('inf')

        while left <= right:
            mid = (left + right) // 2

            hours = testEatingSpeed(mid)

            if hours > h:
                left = mid+1
            else:
                right = mid-1
                minSpeed = min(mid, minSpeed)
        
        return minSpeed
            
            


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numSet = set(nums)
        
        longestStreak = 1
        currentStreak = 1

        for n in numSet:
            if n-1 in numSet:
                    continue
            else:
                increment = 1

                while n+increment in numSet:
                    currentStreak += 1
                    increment += 1

                    longestStreak = max(currentStreak, longestStreak)
                
                currentStreak = 1

        return longestStreak

        





        
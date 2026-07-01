class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        longestStreak = 0
        streak = 1

        for n in nums:
            if n-1 in nums:
                continue
            
            it = 1
            
            while n+it in nums:
                streak += 1
                it += 1
            
            longestStreak = max(streak, longestStreak)
            streak = 1

        return longestStreak



        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        setNums = set(nums)

        longestStreak = 1
        currentStreak = 1

        doNothing = 0

        for n in setNums:
            print(f'start: {n}')
            if (n-1) in setNums:
                continue
            else:
                i = 1
                while (n+i) in setNums:
                    print(n+i)
                    currentStreak += 1
                    i += 1
            
            longestStreak = max(longestStreak, currentStreak)
            currentStreak = 1
        
        return longestStreak



        





        
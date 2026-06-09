class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sortedNums = sorted(list(set(nums)))
        print(sortedNums)

        longestStreak = 1
        currentStreak = 1

        for i in range(0, len(sortedNums) - 1):
            longestStreak = max(longestStreak, currentStreak)

            if sortedNums[i+1] == sortedNums[i] + 1:
                currentStreak += 1
                longestStreak = max(longestStreak, currentStreak)
            else:
                currentStreak = 1
        
        return longestStreak
        





        
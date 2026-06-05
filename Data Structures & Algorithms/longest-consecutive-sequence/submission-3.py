class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = list(set(nums))
        nums.sort()

        print(nums)
        
        maxLen = 1
        currLen = 1
        currNum = nums[0]

        for n in range(1, len(nums)):
            if nums[n] == currNum + 1:
                print(nums[n])
                currLen += 1
                currNum = nums[n]
            else:
                currLen = 1
                currNum = nums[n]
            
            if currLen > maxLen:
                maxLen = currLen
        
        return maxLen
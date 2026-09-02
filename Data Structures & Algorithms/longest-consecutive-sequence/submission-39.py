class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = set(nums)

        curr = 1
        longest = 1

        for n in nums:
            if n-1 in nums:
                continue
            
            i = 1
            while n+i in nums:
                curr += 1
                i += 1
            
            longest = max(longest, curr)
            curr = 1

        return longest


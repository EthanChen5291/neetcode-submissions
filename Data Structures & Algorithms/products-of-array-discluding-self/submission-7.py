class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        # for n in nums, n = product of (left elts) and (right elts)
        res = [1 for _ in range(len(nums))]

        multiplier = nums[0]

        for i in range(1, len(nums)):
            res[i] *= multiplier
            multiplier *= nums[i]
        
        multiplier = nums[len(nums)-1]

        for i in reversed(range(0, len(nums)-1)):
            res[i] *= multiplier
            multiplier *= nums[i]
        
        return res


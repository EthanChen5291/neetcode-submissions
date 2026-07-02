class Solution:
    def findMin(self, nums: List[int]) -> int:
        # maintain middle

        # binary sort on nums:

        # check if right < middle OR middle < left. if so, it flipped and is in that area

        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            if nums[right] < nums[middle]:
                left = middle + 1
            else:
                right = middle

        return nums[left]
             
        
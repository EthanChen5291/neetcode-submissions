class Solution:
    def findMin(self, nums: List[int]) -> int:
        # maintain middle

        # binary sort on nums:

        # check if right < middle OR middle < left. if so, it flipped and is in that area

        left = 0
        right = len(nums) - 1
        minimum = float('inf')

        while left <= right:
            middle = (left + right) // 2

            if nums[right] < nums[middle]:
                left = middle + 1
                minimum = min(nums[right], minimum)
                print(minimum)
            elif nums[middle] < nums[left]:
                right = middle - 1
                minimum = min(nums[middle], minimum)
                print(minimum)
            else:
                right = middle - 1
                minimum = min(nums[middle], minimum)

        return minimum
             
        
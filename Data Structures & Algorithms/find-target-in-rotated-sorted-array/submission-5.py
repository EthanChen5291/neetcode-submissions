class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) -1

        while left <= right:

            # find beginning

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] > nums[right]: # flipped here
                if target <= nums[right] or target > nums[mid]:
                    left = mid+1
                else:
                    right = mid-1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        
        return -1

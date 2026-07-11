class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        left = 0
        right = len(nums)-1

        while left <= right:
            middle = (left+right) // 2

            if nums[middle] == target:
                return middle

            if nums[middle] > nums[right]: # that side is flipped
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
            
        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search on nums


        # if middle < right:
        # if target > middle: 
        # shift left to middle

        # if left < middle:
        # if target < middle:
        # shift right to middle

        # if left > middle:
        # restarts
        # 4 5 1 2 3

        # if one side repeats, the other side is sorted
        # so if target > right or target < left, target must be in left side

        left = 0
        right = len(nums) - 1

        while left <= right:
            
            #check which side is sorted
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            if nums[middle] < nums[right]:
                if nums[middle] < target <= nums[right]:
                    left = middle+1
                else:
                    right = middle-1
            else:
                if nums[left] <= target < nums[middle]:
                    right = middle-1
                else:
                    left = middle+1
        
        return -1



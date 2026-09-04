class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        # find side that repeats (outer bounds contradict each other)
        # then find beginning

        left = 0
        right = len(nums)-1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]: # restart in right half
                left = mid+1
            else:
                right = mid
        
        return nums[left]
        


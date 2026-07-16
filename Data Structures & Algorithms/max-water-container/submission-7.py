class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        maxArea = 0

        while left < right:
            dist = right - left
            height = min(heights[left], heights[right])

            area = dist * height
            maxArea = max(area, maxArea)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea



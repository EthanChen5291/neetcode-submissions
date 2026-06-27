class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        maxVolume = 0
        currentVol = 0

        while left < right:
            dist = right - left
            height = min(heights[left], heights[right])

            currentVol = dist * height

            maxVolume = max(currentVol, maxVolume)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return maxVolume

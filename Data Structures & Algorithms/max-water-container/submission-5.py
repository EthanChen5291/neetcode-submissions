class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVolume = 0
        currentVolume = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            dist = right - left
            height = min(heights[left], heights[right])

            currentVolume = height * dist
            print(f'left: {left}, right: {right}, height: {height}')

            maxVolume = max(maxVolume, currentVolume)
            
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return maxVolume


        
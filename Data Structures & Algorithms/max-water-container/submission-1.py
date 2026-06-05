class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currentMax = 0
        left = 0
        right = len(heights) - 1
        distance = right - left
        maxArea = 0
        currentArea = 0

        while left < right:
            currentArea = (right - left) * min(heights[left],heights[right])
            print("left:" + str(left))
            print("right:" + str(right))
            print(currentArea)
            if currentArea > maxArea:
                maxArea = currentArea
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea




        
        
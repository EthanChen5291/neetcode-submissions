class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        seenMap = {}
        maxLen = 1

        left = 0
        for i, char in enumerate(s):
            if char in seenMap and seenMap[char] >= left:
                left = seenMap[char] + 1

            seenMap[char] = i

            winLen = i - left + 1
            maxLen = max(maxLen, winLen)

        return maxLen

            

            



                


        

        

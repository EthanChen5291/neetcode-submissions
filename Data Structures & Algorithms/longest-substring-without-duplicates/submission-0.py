class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        seenMap = {}
        left = 0
        streak = 1

        for right in range(len(s)):
            c = s[right]

            if c in seenMap and seenMap[c] >= left:
                left = seenMap[c] + 1
            
            seenMap[c] = right
            window = right - left + 1
            streak = max(streak, window)
        
        return streak


        

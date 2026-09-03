class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seenMap = {} # char : indices

        left = 0

        longest = 0

        for right in range(len(s)):
            char = s[right]

            if char in seenMap and left <= seenMap[char] < right:
                prev = seenMap[char]
                left = prev + 1

            seenMap[char] = right

            longest = max(longest, right - left + 1)
        
        return longest
                
                
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        maxCharCount = 0
        left = 0

        seenMap = {} # char : counts

        for right in range(len(s)):
            char = s[right]

            seenMap[char] = seenMap.get(char, 0) + 1
            maxCharCount = max(maxCharCount, seenMap[char])

            while (right - left + 1) - k > maxCharCount:
                seenMap[s[left]] -= 1 #need to somehow update maxCharCount
                left += 1
        
            longest = max(longest, right - left + 1)
        
        return longest
            


                
        


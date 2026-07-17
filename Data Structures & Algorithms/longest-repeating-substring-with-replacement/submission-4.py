class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window approach
        # win_len + k = most common char
        maxLen = 0
        commonCharCount = 0

        left = 0

        seenMap = {}

        for i, char in enumerate(s):
            seenMap[char] = seenMap.get(char, 0) + 1

            if seenMap[char] >= commonCharCount:
                commonCharCount = seenMap[char]

            while (i - left) - commonCharCount >= k:
                seenMap[s[left]] -= 1
                left += 1
            
            winLen = i - left + 1
            maxLen = max(maxLen, winLen)

        return maxLen




        
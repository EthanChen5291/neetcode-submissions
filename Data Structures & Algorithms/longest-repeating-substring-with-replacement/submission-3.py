class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # countMap -> maintained throughout
        # countMap kept for s and k and compared
        
        # mostFreqCharCount - while iterating, check if mostFreqCharCount < countMap[c]

        # if mostFreqCharCount + k < windowSize, then must move left up until not true
        # also decrement countMap[c]
        countMap = {}
        left = 0

        longest = 0
        mostFreqCharCount = 0

        for right in range(len(s)):
            char = s[right]
            countMap[char] = countMap.get(char, 0) + 1

            if countMap[char] > mostFreqCharCount:
                mostFreqCharCount = countMap[char]

            while mostFreqCharCount + k < right - left + 1:
                countMap[s[left]] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)
        
        return longest





        
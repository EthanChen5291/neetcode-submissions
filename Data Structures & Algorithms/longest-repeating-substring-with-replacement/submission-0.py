class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window here
        # hash for incrementing (diffs)
        # how to "know" the repeating character?

        # window = streak
        # iterate until diffChars == k then return len(window)

        left = 0
        longestStreak = 1
        seenMap = {}

        mostFreqChar = ''
        mostFreqCharCount = 0

        for right in range(len(s)):
            c = s[right]
            seenMap[c] = seenMap.get(c, 0) + 1
            
            mostFreqCharCount = max(mostFreqCharCount, seenMap[c])

            window = right - left + 1

            while window - k > mostFreqCharCount:
                seenMap[s[left]] -= 1
                left += 1
                window = right - left + 1

            longestStreak = max(longestStreak, right - left + 1)
            
        return longestStreak




        
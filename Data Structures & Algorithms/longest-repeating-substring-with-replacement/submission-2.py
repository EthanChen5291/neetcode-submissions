class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # mostFreqChar -> compare with seenMap[c] each iteration

        # mostFreqChar + k <= window

        # longest = max(longest, window)

        # whenever mostFreqChar + k > window,
        #   while this is true left += 1

        # seenMap hold char counts

        countMap = {}
        mostFreqCharCount = 0
        longest = 1
        left = 0

        for i, c in enumerate(s):
            countMap[c] = countMap.get(c, 0) + 1

            if countMap[c] > mostFreqCharCount:
                mostFreqCharCount = countMap[c]

            while mostFreqCharCount + k < (i - left + 1):
                countMap[s[left]] -= 1
                left += 1
            
            longest = max(i - left + 1, longest)

        return longest

        



        
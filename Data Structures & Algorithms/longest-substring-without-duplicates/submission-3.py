class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenMap = {}
        left = 0
        longest = 0

        for i,c in enumerate(s):
            if c in seenMap and seenMap[c] >= left:
                left = seenMap[c] + 1
                print(seenMap[c])
            
            seenMap[c] = i

            window = i - left + 1
            longest = max(window, longest)

        return longest


        
            

                


        

        

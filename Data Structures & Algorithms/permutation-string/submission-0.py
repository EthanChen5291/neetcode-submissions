class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if not s2:
            return False
        if not s1:
            return True # hesitantly

        left = 0
        
        s1Map = self.getIndexMap(s1)

        windowSize = len(s1) - 1
        s2Map = self.getIndexMap(s2[:windowSize])

        for right in range(windowSize, len(s2)):
            rightChar = s2[right]
            s2Map[rightChar] = s2Map.get(rightChar, 0) + 1
            
            if s2Map == s1Map:
                return True

            leftChar = s2[left]

            if s2Map[leftChar] - 1 <= 0:
                del s2Map[leftChar]
            else:
                s2Map[leftChar] -= 1

            left += 1
        
        return False

    
    def getIndexMap(self, s: str) -> dict:
        indexMap = {}

        for c in s:
            indexMap[c] = indexMap.get(c, 0) + 1
        
        return indexMap

            


        
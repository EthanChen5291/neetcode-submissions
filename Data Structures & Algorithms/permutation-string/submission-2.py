class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = self.getIndexMap(s1)
        offset = len(s1)

        s2Map = self.getIndexMap(s2[:offset])

        if s1Map == s2Map:
            return True

        left = 0
        for i in range(offset, len(s2)):

            # increment left pointer
            leftCharCount = s2Map[s2[left]]
            if leftCharCount - 1 == 0:
                del s2Map[s2[left]]
            else:
                s2Map[s2[left]] -= 1
            left += 1

            # increment right pointer
            rightElt = s2[i]
            s2Map[rightElt] = s2Map.get(rightElt, 0) + 1

            if s1Map == s2Map:
                return True
        
        return False
            
    def getIndexMap(self, s: str) -> dict:
        indexMap = {}

        for char in s:
            indexMap[char] = indexMap.get(char, 0) + 1
        
        return indexMap


        
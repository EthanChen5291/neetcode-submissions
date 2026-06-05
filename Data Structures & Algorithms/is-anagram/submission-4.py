class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        indexMap = {}

        def getIndexMap(s: str) -> dict:
            indexMap = {}

            for c in s:
                if c in indexMap:
                    indexMap[c] += 1
                else:
                    indexMap[c] = 1
            
            return indexMap

        if getIndexMap(s) == getIndexMap(t):
            return True
        else:
            return False

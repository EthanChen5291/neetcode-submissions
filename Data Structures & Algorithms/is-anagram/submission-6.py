class Solution:
    def isAnagram(self, s: str, t: str) -> bool:



        def indexMap(s: str) -> dict:
            idxMap = {}
            
            for c in s:
                if not c in idxMap:
                    idxMap[c] = 0

                idxMap[c] += 1
            
            return idxMap
        
        return indexMap(s) == indexMap(t)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def indexMap(s: str) -> dict:
            chars = list(s)
            indexMap = dict()

            for c in chars:
                if c in indexMap:
                    indexMap[c] += 1
                else:
                    indexMap[c] = 1
            
            return indexMap
        
        if indexMap(s) == indexMap(t):
            return True

        return False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def indexMap(s: str) -> dict:
            idxMap = {}

            for c in s:
                idxMap[c] = idxMap.get(c, 0) + 1

            return idxMap
        
        if len(s1) > len(s2):
            return False

        s1Map = indexMap(s1)
        s2Map = indexMap(s2[:len(s1)])

        if s1Map == s2Map:
            return True

        for i in range(len(s1),len(s2)):            
            char = s2[i]
            s2Map[char] = s2Map.get(char, 0) + 1

            leftChar = s2[i - len(s1)]
            s2Map[leftChar] -= 1

            if s2Map[leftChar] == 0:
                del s2Map[leftChar]
            
            if s1Map == s2Map:
                return True
        
        return False
            
        
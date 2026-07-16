class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.getIndexMap(s) == self.getIndexMap(t)

    def getIndexMap(self, s: str) -> dict:
        indexMap = {}

        for c in s:
            indexMap[c] = indexMap.get(c, 0) + 1

        return indexMap


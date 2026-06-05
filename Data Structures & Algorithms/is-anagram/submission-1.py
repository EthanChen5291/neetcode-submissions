class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        def createIndexList(word: str) -> dict:
            indexList = {}

            for char in word:
                if char in indexList:
                    indexList[char] += 1
                else:
                    indexList[char] = 1
                
            return indexList

        def valid(word: str, indexList: dict) -> bool:
            for char in word:
                if char in indexList and indexList[char] >= 1:
                    indexList[char] -= 1
                else:
                    return False
            
            return True
            
        indexList = createIndexList(s)
        return valid(t, indexList)

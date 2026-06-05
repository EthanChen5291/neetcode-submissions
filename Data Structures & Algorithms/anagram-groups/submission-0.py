import copy

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDicts = [self.makeWordDict(s) for s in strs]

        anagramGroups = []
        visited = [False] * len(strs)

        for i in range(0, len(strs)):
            if visited[i]:
                continue
            
            currentGroup = [strs[i]]
            visited[i] = True

            for j in range(i + 1, len(strs)):
                if not visited[j]:
                    if wordDicts[i] == wordDicts[j]:
                        currentGroup.append(strs[j])
                        visited[j] = True
            
            anagramGroups.append(currentGroup)
        
        return anagramGroups

    def makeWordDict(self, word: str) -> dict:
        wordDict = {}
        for char in word:
            if char in wordDict:
                wordDict[char] += 1
            else:
                wordDict[char] = 1
        return wordDict
            
    def validAnagram(self, w1: str, w2: str, w1Dict: dict) -> bool:
        copy_dict = copy.deepcopy(w1Dict)

        if len(w1) != len(w2):
            return False

        for char in w2:
            if char in copy_dict and copy_dict[char] > 0:
                copy_dict[char] -= 1
            else:
                return False
        
        return True
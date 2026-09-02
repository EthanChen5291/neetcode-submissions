class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap = {}

        for word in strs:
            key = "".join(sorted(word))

            if key in wordMap:
                wordMap[key].append(word)
            else:
                wordMap[key] = [word]
        
        res = []
        
        for key, val in wordMap.items():
            res.append(val)
        
        return res
        


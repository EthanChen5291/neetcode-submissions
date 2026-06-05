class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        indexMap = {}

        for s in strs:
            sortedStr = "".join(sorted(s))

            if sortedStr in indexMap:
                indexMap[sortedStr].append(s)
            else: 
                indexMap[sortedStr] = [s]

        res = []
        for key, s in indexMap.items():
            res.append(s)
        
        return res
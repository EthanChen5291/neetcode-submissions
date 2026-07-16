class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keyMap = {}

        for s in strs:
            key = "".join(sorted(s))

            if key in keyMap:
                keyMap[key].append(s)
            else:
                keyMap[key] = [s]
            
        res = []

        for key, val in keyMap.items():
            res.append(val)
        
        return res
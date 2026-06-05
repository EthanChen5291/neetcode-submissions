class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        indexMap = {}

        for s in strs:
            sortedS = "".join(sorted(s))

            if sortedS in indexMap:
                indexMap[sortedS].append(s)
            else:
                indexMap[sortedS] = [s]
            
        return [s[1] for s in indexMap.items()]

        # get indexMap

        # if indexMap in dict:

        # append to dict

        #then, grab all values of dict
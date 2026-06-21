class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = {}

        for n in nums:
            if n in frequencyMap: 
                frequencyMap[n] += 1
            else:
                frequencyMap[n] = 1
        
        return sorted(frequencyMap, reverse=True, key=frequencyMap.get)[:k]
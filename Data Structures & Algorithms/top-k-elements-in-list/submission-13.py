class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        indexMap = {}

        for n in nums:
            if n in indexMap:
                indexMap[n] += 1
            else:
                indexMap[n] = 1
            
        sortedItems = sorted(indexMap.items(), key=lambda x: x[1], reverse=True)
        return [n[0] for n in sortedItems][:k]
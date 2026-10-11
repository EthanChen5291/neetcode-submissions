class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}

        for i, n in enumerate(nums):
            countMap[n] = countMap.get(n, 0) + 1

        totalEntries = sorted(countMap.items(), reverse=True, key=lambda x: x[1])

        return [x[0] for x in totalEntries[:k]]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}

        for n in nums:
            countMap[n] = countMap.get(n, 0) + 1

        res = sorted(countMap.items(), key=lambda x: x[1], reverse=True)[:k]

        return [n[0] for n in res]
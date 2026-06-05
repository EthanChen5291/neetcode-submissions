class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}

        for n in nums:
            countMap[n] = countMap.get(n, 0) + 1
        
        sortedList = sorted(
            countMap.items(),
            reverse=True,
            key=lambda i: i[1]
        )

        return [i[0] for i in sortedList[:k]]



        
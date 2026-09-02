from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        # num : occurrences

        sortedList = sorted(counter.items(), reverse=True, key=lambda n: n[1])

        return [n[0] for n in sortedList[:k]]

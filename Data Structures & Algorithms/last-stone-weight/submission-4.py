class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        weights = [-s for s in stones]

        heapq.heapify(weights)

        while len(weights) > 1:
            s1 = abs(heapq.heappop(weights))
            s2 = abs(heapq.heappop(weights))

            if s1 == s2:
                continue
            elif s1 < s2:
                heapq.heappush(weights, -(s2 - s1))
            else:
                heapq.heappush(weights, -(s1 - s2))
        
        if weights:
            return abs(weights[0])
        
        return 0
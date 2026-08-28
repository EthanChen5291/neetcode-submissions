class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)



        # max heap

        while len(stones) > 1:
            first = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)

            if first == second:
                continue
            elif first < second:
                heapq.heappush_max(stones, second - first)
            else:
                heapq.heappush_max(stones, first - second)
            
        return stones[0] if stones else 0

        

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def distanceFromOrigin(x: int, y: int) -> int:
            return x**2 + y**2

        total = [(distanceFromOrigin(p[0], p[1]), p) for p in points]

        heapq.heapify(total)

        res = []

        for i in range(k):
            val = heapq.heappop(total)

            res.append(val[1])
        
        return res
            

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for p in points:
            p.insert(0, self.distanceFromOrigin(p))

        heapq.heapify(points)

        res = []

        while len(res) < k:
            num = heapq.heappop(points)
            num.pop(0)
            res.append(num)
        
        return res

    
    def distanceFromOrigin(self, point: List[int]) -> int:
        x1 = point[0]
        y1 = point[1]

        return (x1 - 0)**2 + (y1 - 0)**2

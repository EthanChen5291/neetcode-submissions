class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        sol = []

        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        
        uq = list(set(nums))
        tuples = []

        for num in uq:
            tuples.append((d[num], num))

        tuples = sorted(tuples, reverse=True, key=lambda x: x[0])
        
        seen = set()
        
        for i in range(k):
            best = tuples.pop(0)
            sol.append(best[1])
        
        return sol


            
        
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
        
        seen = set()
        
        for i in range(k):
            best = max(tuples, key=lambda x: x[0])
            print(best)
            i = tuples.index(best)
            sol.append(tuples.pop(i)[1])
        
        return sol


            
        
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures);
        res = []

        for i in range(0, l):
            for j in range(i, l):
                if temperatures[j] > temperatures[i]:
                    print(f"i: {i}, j: {j}")
                    res.append(j - i)
                    break

            
            if len(res) <= i:
                res.append(0)
        
        return res
        

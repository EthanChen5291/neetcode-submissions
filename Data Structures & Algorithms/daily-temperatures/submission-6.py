class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for t in temperatures]
        stack = [] 

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                lastTemp, lastIdx = stack.pop()
                res[lastIdx] = i - lastIdx
            
            stack.append((t, i))
        
        return res

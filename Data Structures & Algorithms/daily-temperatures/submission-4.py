class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for t in temperatures]
        stack = []

        for i, t in enumerate(temperatures):
            
            while stack and t > stack[-1][0]:
                oldTempIdx = stack.pop()[1]
                res[oldTempIdx] = i - oldTempIdx
            
            stack.append((t, i))
        
        return res



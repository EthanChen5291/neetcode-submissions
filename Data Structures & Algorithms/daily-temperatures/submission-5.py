class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for t in temperatures]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                prevTemp = stack[-1][1]

                daysAfter = i - prevTemp
                res[prevTemp] = daysAfter

                stack.pop()

            stack.append((t, i))
        
        return res
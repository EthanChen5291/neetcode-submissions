class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures);
        res = [0 for i in range(l)]

        stack = []

        # temperatures -> random
        # follows time

        # less than last on stack
        # free stack until local max < stack[i]

        # 1 5 3 6 8
        # 1 5 3 6 8

        for i in range(l):
            while stack and temperatures[i] > stack[-1][0]:
                #print(stack[-1][0])
                print(f"{i}, {stack}")
                next = stack.pop()[1]
                res[next] = i - next
                print(f"{i}, {stack}, {next}")
                #print(res)
            
            stack.append((temperatures[i], i))
            

        stackLen = len(stack)
        
        return res
        

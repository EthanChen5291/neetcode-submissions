class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # for elt in temps, iterate until warmer temp

        # -- optimal

        currentTemps = [] # list[(temp, index)]
        res = [0 for i in temperatures]

        # when we find a warmer day, pop from stack
        # enumerate 

        for i, t in enumerate(temperatures):
            while currentTemps and currentTemps[-1][0] < t:
                tup = currentTemps.pop()
                print(f'{t} is warmer than {tup[0]} and is {i - tup[1]} days after')

                temp = tup[0]
                daysSince = i - tup[1]
                res[tup[1]] = daysSince
            else:
                currentTemps.append((t, i))

        return res


    
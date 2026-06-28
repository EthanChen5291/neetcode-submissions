class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # iterate backwards

        # if speed of car [i-1] < speed of car [i] then it's a car fleet 

        pos, spd = zip(*sorted(zip(position, speed), reverse=True))

        pos = list(pos)
        spd = list(spd)

        fleets = 0
        slowestTime = 0

        for i in range(len(pos)):
            time = (target - pos[i]) / spd[i]

            if time > slowestTime:
                fleets += 1
                slowestTime = time
            
        return fleets

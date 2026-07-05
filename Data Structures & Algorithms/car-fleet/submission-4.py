class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True) 
        # groups cars and sorts by distance from target ascending

        fleets = 0
        slowestTimeAhead = 0

        for pos, spd in cars:
            time = (target - pos) / spd

            if time > slowestTimeAhead:
                fleets += 1
                slowestTimeAhead = time
            
        return fleets





class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # target -> set checkpoint
        
        # cars travel 0->inf

        # fleet -> slowest time
        # time to destination -> (target - position) / speed

        cars = sorted(
            zip(position, speed), 
            reverse=True, 
            key=lambda c: c[0])
        
        fleets = 0
        slowestTimeAhead = 0
        
        for pos, spd in cars: # walk in descending order
            time = (target - pos) / spd

            if time > slowestTimeAhead:
                slowestTimeAhead = time
                fleets += 1
        
        return fleets
            


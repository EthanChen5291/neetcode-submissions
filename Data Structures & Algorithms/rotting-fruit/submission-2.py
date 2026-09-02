from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs from rotten fruit

        # obtain rotten fruit

        rotten = []
        fresh = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                elif grid[r][c] == 1:
                    fresh.add((r, c))

        queue = deque()

        queue += rotten
        minutes = 0
        # apply bfs to rotten 

        while queue and fresh:
            l = len(queue)

            for _ in range(l):
                r, c = queue.popleft()

                for nr, nc in [
                    (r+1, c),
                    (r-1, c),
                    (r, c+1),
                    (r, c-1)
                ]:
                    if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
                        continue
                    
                    if grid[nr][nc] != 1:
                        continue
                    
                    grid[nr][nc] = 2
                    fresh.remove((nr, nc))
                    queue.append((nr, nc))
            
            minutes += 1
        
        if fresh:
            return -1

        return minutes


        
                    

                    
                

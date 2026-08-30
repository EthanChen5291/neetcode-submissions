from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # impossible if fresh fruit not next to rotting fruit

        # bfs starting from rotten fruit. 

        # if still fresh fruit, 

        queue = deque()

        fresh = set()

        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                val = grid[r][c]

                if val == 1:
                    fresh.add((r, c))
                elif val == 2:
                    queue.append((r, c))
        
        while queue and fresh:
            levelSize = len(queue)

            for _ in range(levelSize):
                r, c = queue.popleft()

                for row, col in [
                    (r+1, c),
                    (r-1, c),
                    (r, c+1),
                    (r, c-1)
                ]:
                    outOfBounds = (row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]))
                    if not outOfBounds and grid[row][col] == 1:
                        grid[row][col] = 2
                        fresh.remove((row, col))
                        queue.append((row, col))
            
            time += 1

        if fresh:
            return -1

        return time
                
                    

                    
                
        

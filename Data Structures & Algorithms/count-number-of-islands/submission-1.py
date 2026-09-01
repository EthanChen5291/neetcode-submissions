from typing import Optional

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0


        # increment islands
        # then do bfs, where bfs gets rid of island

        def bfs(r: int, c: int, grid: List[List[str]]) -> None:
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return 

            if grid[r][c] != '1':
                return 
            
            grid[r][c] = '0'

            for nr, nc in [
                (r+1, c),
                (r-1, c),
                (r, c+1),
                (r, c-1)
            ]:
                bfs(nr, nc, grid)

        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    islands += 1
                    bfs(r, c, grid)
        
        return islands


            
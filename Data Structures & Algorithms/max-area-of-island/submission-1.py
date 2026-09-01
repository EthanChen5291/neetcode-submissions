class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        def dfs(r: int, c: int) -> int:
            if not (
                0 <= r < len(grid) and
                0 <= c < len(grid[0])
            ):
                return 0
            
            if grid[r][c] != 1:
                return 0
            
            grid[r][c] = 0

            area = 1
            
            for nr, nc in (
                (r+1, c),
                (r-1, c),
                (r, c+1),
                (r, c-1)
            ):
                area += dfs(nr, nc)
            
            return area
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    maxArea = max(maxArea, area)
        
        return maxArea


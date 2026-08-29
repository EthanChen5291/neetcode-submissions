class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def areaOfIsland(r: int, c: int, grid: List[List[int]]) -> int:
            maxRows = len(grid)
            maxCols = len(grid[0])

            if (r < 0) or (c < 0) or (r >= maxRows) or (c >= maxCols):
                return 0
            
            if grid[r][c] != 1:
                return 0
            
            grid[r][c] = 0

            down = areaOfIsland(r+1, c, grid)
            up = areaOfIsland(r-1, c, grid)
            right = areaOfIsland(r, c+1, grid)
            left = areaOfIsland(r, c-1, grid)

            return 1 + down + up + left + right
        
        maxArea = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                val = grid[r][c]

                if val == 1:
                    area = areaOfIsland(r, c, grid)

                    maxArea = max(maxArea, area)

        return maxArea


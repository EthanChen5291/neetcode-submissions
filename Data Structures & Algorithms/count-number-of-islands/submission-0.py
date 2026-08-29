class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # two points are connected if abs(r2 - r1) <= 1 and abs(c2 - c1) <= 1

        # will have to check all around the islands for connections

        #if i find one island, i need to know where i havent explored yet

        # iterate through the grid, add only if there arent surrounding islands

        def dfs(r: int, c: int, grid: List[List[int]]) -> None:
            maxRows = len(grid)
            maxCols = len(grid[0])

            if (r < 0 or c < 0) or (r >= maxRows or c >= maxCols):
                return 
            
            if (grid[r][c] != '1'):
                return
            
            grid[r][c] = '0'

            dfs(r+1,c, grid)
            dfs(r-1,c, grid)
            dfs(r, c+1, grid)
            dfs(r, c-1, grid)

        count = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                val = grid[r][c]

                if val == '1':
                    count += 1
                    dfs(r, c, grid)
        
        return count




            
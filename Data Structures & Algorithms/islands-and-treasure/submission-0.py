class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #bfs?

        # for every land cell, go in an outwards ring until u reach a treasure chest

        # or hash the locations of all treasures chests and identify closest 

        # dfs? go closer by iterating index until u reach treasure chest

        LAND = 2147483647
        queue = []

        for r in range(len(grid)): #O(n)
            for c in range(len(grid[0])):
                val = grid[r][c]

                if val == 0:
                    queue.append((r, c))

        distance = 0
        
        while queue:
            l = len(queue)

            for i in range(l):
                r, c = queue.pop(0)
                
                above = (r-1, c)
                below = (r+1, c)
                right = (r, c+1)
                left = (r, c-1)

                for row, col in [above, below, right, left]:
                    if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]):               
                        if grid[row][col] == LAND:
                            grid[row][col] = distance + 1
                            queue.append((row, col))
            
            distance += 1
        
        return



                        

                    
                    







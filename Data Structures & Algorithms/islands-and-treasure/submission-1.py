class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        land = 2147483647

        # bfs from treasure chests
        def fillLand() -> None:
            queue = deque()
            distance = 1

            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c] == 0:
                        queue.append((r, c))

            while queue:
                l = len(queue) 

                for i in range(l):
                    r, c = queue.popleft()

                    for nr, nc in [
                        (r+1, c),
                        (r-1, c),
                        (r, c+1),
                        (r, c-1)
                    ]:
                        if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
                            continue
                        
                        if grid[nr][nc] != land:
                            continue
                        
                        grid[nr][nc] = distance
                        queue.append((nr, nc))
                
                distance += 1

        fillLand()

        return



                        

                    
                    







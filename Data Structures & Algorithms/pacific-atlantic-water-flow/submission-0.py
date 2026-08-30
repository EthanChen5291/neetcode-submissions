from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        #iterate through heights, run bfs on every tile

        # - reachable through neighbors ()

        # - reachesPacific -> if reaches node with r == 0 or c == 0
        # - reachesAtlantic -> if reaches node with r == maxRows - 1 or c == maxCols - 1

        # for any given node, it must fullfil those two checklists
        # maintain sets


        reachesPacific = set()
        reachesAtlantic = set()

        maxRows = len(heights)
        maxCols = len(heights[0])

        res = []
        
        for r in range(maxRows):
            for c in range(maxCols):
                queue = deque([(r, c)])
                visited = {(r,c)}

                reachesPacific = False
                reachesAtlantic = False

                while queue:
                    currR, currC = queue.popleft()

                    if (currR == 0 or currC == 0):
                        reachesPacific = True
                    
                    if currR == maxRows - 1 or currC == maxCols - 1:
                        reachesAtlantic = True
                    
                    if reachesPacific and reachesAtlantic:
                        res.append([r, c])
                        break

                    for nr, nc in [
                        (currR+1, currC),
                        (currR-1, currC),
                        (currR, currC+1),
                        (currR, currC-1)
                    ]:
                        if nc < 0 or nr < 0 or nc >= maxCols or nr >= maxRows or (nr, nc) in visited:
                            continue 

                        if heights[nr][nc] <= heights[currR][currC]:
                            visited.add((nr, nc))
                            queue.append((nr, nc))
            
        return res
            


        
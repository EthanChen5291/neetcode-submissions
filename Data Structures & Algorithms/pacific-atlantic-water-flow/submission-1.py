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

        queue = deque()
        
        for r in range(len(heights)):
            queue.append((r, 0))
        
        for c in range(len(heights[0])):
            queue.append((0, c))

        reachesPacific = self.bfs(queue, heights)
        
        for r in range(len(heights)):
            queue.append((r, len(heights[0])-1))
        
        for c in range(len(heights[0])):
            queue.append((len(heights)-1, c))
        
        reachesAtlantic = self.bfs(queue, heights)
        
        return [p for p in reachesAtlantic if p in reachesPacific]
        

        
    def bfs(self, queue: List[tuple(int, int)], heights: List[List[int]]) -> list[tuple(int, int)]: # takes border points, returns all points the border points connected to in heights
        visited = set()
        for q in queue:
            visited.add(q)

        while queue:
            r, c = queue.popleft()

            for nr, nc in [
                (r+1, c),
                (r-1, c),
                (r, c+1),
                (r, c-1)
            ]:
                if nr < 0 or nc < 0 or nr >= len(heights) or nc >= len(heights[0]) or (nr, nc) in visited:
                    continue
                
                if heights[nr][nc] >= heights[r][c]:
                    queue.append((nr, nc))
                    visited.add((nr, nc))
                

        return visited






            


        
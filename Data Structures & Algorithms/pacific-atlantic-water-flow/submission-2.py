from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:



        
        #figure out which cells the pacific reaches and which the atlantic reaches
        pacific = deque()
        atlantic = deque()

        for r in range(len(heights)):
            pacific.append((r, 0))
            atlantic.append((r, len(heights[0])-1))
        
        for c in range(len(heights[0])):
            pacific.append((0, c))
            atlantic.append((len(heights)-1, c))

        def bfs(queue) -> set:
            queue
            
            visited = set()

            while queue:
                r, c = queue.popleft()
                visited.add((r, c))

                for nr, nc in [
                    (r+1, c),
                    (r-1, c),
                    (r, c+1),
                    (r, c-1)
                ]:
                    if not (0 <= nr < len(heights) and 0 <= nc < len(heights[0])):
                        continue
                    
                    if (nr, nc) in visited:
                        continue
                    
                    if heights[nr][nc] < heights[r][c]:
                        continue
                    
                    queue.append((nr, nc))
            
            return visited
        
        reachesPacific = bfs(pacific)
        reachesAtlantic = bfs(atlantic)

        return [i for i in reachesPacific if i in reachesAtlantic]





            


        
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # get rid of 'O' cells that aren't on edge

        # use bfs to get rid of 'O' cells, unless one is found on edge
        # -> cannot remove until verified that there is no edge
        # maybe keep a visited tree, remove v in visited if no queue

        def bfs(r, c) -> None:
            queue = deque()

            queue.append((r, c))
            visited = set()
            hasEdge = False

            while queue:

                r, c = queue.popleft() # verified to be an O

                edgeCell = (r == 0 or r == len(board)-1 or c == 0 or c == len(board[0])-1)

                if edgeCell:
                    hasEdge = True

                visited.add((r, c))
                for nr, nc in [
                    (r+1, c),
                    (r-1, c),
                    (r, c+1),
                    (r, c-1)
                ]: 
                    if not (0 <= nr < len(board) and 0 <= nc < len(board[0])):
                        continue
                    
                    if (nr, nc) in visited:
                        continue
                    
                    if not board[nr][nc] == 'O':
                        continue
                    
                    queue.append((nr, nc))
                    visited.add((nr, nc))
            
            if not hasEdge:
                for r, c in visited:
                    board[r][c] = 'X'
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    bfs(r, c)
        
        return

            

                    
                    
                    

                    




        



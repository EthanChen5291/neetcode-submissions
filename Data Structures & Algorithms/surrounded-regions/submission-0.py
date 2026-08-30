class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # do not capture if region has any edge cells
        
        # find 'O's by iterating through board

        # iterate through the 'O's through bfs -> if no edge cells, capture

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board = self.bfs(r, c, board)
        
        return

        
    def bfs(self, r, c, board) -> List[List[int]]:
        # iterate through the 'O's through bfs -> if no edge cells, capture
        
        queue = deque()
        queue.append((r, c))
        
        visited = {(r, c)}

        hasEdge = False

        while queue:
            r, c = queue.popleft()

            if ( 
                    r == 0 or 
                    r == len(board)-1 or 
                    c == 0 or 
                    c == len(board[0])-1
                ):

                    hasEdge = True
                    # found an edge cell, do not destroy

            for nr, nc in [
                (r+1, c),
                (r-1, c),
                (r, c+1),
                (r, c-1)
            ]:
                if (
                    nr < 0 or 
                    nc < 0 or 
                    nr >= len(board) or 
                    nc >= len(board[0]) or 
                    (nr, nc) in visited
                ):
                    continue
                
                if board[nr][nc] != "O":
                    continue
                
                queue.append((nr, nc))
                visited.add((nr, nc))
            
        if not hasEdge:
            for r, c in visited:
                board[r][c] = "X"
        
        return board
                

        


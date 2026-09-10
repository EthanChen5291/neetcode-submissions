class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        numRows = len(board)
        numCols = len(board[0])

        # do bfs from all first letter matches at once

        def dfs(r, c, visited, idx): 
            if idx == len(word):
                return True
            
            for nr, nc in [
                (r+1, c),
                (r-1, c),
                (r, c+1),
                (r, c-1)
            ]:
                if not (0 <= nr < numRows and 0 <= nc < numCols):
                    continue

                if board[nr][nc] != word[idx]:
                    continue
                
                if (nr, nc) in visited:
                    continue
                
                visited.add((nr, nc))

                if dfs(nr, nc, visited, idx+1):
                    return True
                
                visited.remove((nr, nc))
            
            return False

        for r in range(numRows):
            for c in range(numCols):
                if board[r][c] == word[0]:
                    if dfs(r, c, {(r, c)}, 1):
                        return True
        
        return False





                    
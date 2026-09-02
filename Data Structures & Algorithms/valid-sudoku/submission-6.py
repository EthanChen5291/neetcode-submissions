class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return True
        
        rowMap = {}
        colMap = {}
        squareMap = {}

        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]

                if val == '.':
                    continue 
                
                if (r in rowMap) and (val in rowMap[r]):
                    return False
                
                if (c in colMap) and (val in colMap[c]):
                    return False
                
                square = (r // 3, c // 3)

                if (square in squareMap) and (val in squareMap[square]):
                    return False
                
                if not r in rowMap:
                    rowMap[r] = [val]
                else:
                    rowMap[r].append(val)

                if not c in colMap:
                    colMap[c] = [val]
                else:
                    colMap[c].append(val)

                if not square in squareMap:
                    squareMap[square] = [val]
                else:
                    squareMap[square].append(val)
        
        return True

                
        
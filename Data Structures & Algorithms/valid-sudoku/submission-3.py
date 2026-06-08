class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squareMap = {}
        rowMap = {}
        colMap = {}

        for row in range(0, len(board)):
            for col in range(0, len(board[0])):
                n = board[row][col]

                if n != '.':
                    
                    square = (row // 3, col // 3)

                    seenInSquare = True if (square in squareMap) and (n in squareMap[square]) else False
                    
                    seenInRow = True if (row in rowMap) and (n in rowMap[row]) else False

                    seenInCol = True if (col in colMap) and (n in colMap[col]) else False

                    if seenInSquare or seenInRow or seenInCol:
                        return False
                    
                    # -- update maps

                    if square in squareMap:
                        squareMap[square].append(n)
                    else:
                        squareMap[square] = [n]
                    
                    if col in colMap:
                        colMap[col].append(n)
                    else:
                        colMap[col] = [n]
                    
                    if row in rowMap:
                        rowMap[row].append(n)
                    else:
                        rowMap[row] = [n]
        
        return True

                        



            
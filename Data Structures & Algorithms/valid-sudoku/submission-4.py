class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = {}
        colMap = {}
        squareMap = {}

        for row in range(len(board)):
            for col in range(len(board[0])):
                elt = board[row][col]

                if elt != '.':
                    square = (row // 3, col // 3)

                    if square in squareMap and elt in squareMap[square]:
                        return False
                    if row in rowMap and elt in rowMap[row]:
                        return False
                    elif col in colMap and elt in colMap[col]:
                        return False
                    
                    if row in rowMap: 
                        rowMap[row].append(elt)
                    else:
                        rowMap[row] = [elt]

                    if col in colMap: 
                        colMap[col].append(elt)
                    else:
                        colMap[col] = [elt]

                    if square in squareMap: 
                        squareMap[square].append(elt)
                    else:
                        squareMap[square] = [elt]
        
        return True

                        



            
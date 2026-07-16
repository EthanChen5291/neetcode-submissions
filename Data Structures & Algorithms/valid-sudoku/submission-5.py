from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        squareMap = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):
                elt = board[row][col]

                if elt == '.':
                    continue
                
                square = (row // 3, col // 3)

                if elt in squareMap[square] or elt in colMap[col] or elt in rowMap[row]:
                    return False
                else:
                    squareMap[square].add(elt)
                    rowMap[row].add(elt)
                    colMap[col].add(elt)
        
        return True


                        



            
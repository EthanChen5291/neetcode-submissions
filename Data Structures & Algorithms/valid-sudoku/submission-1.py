class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # indexMap that records all combinations of values
        seen = set()

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num != ".":
                    rowKey = (row, num)
                    colKey = (num, col)
                    squareKey = (row // 3, col // 3, num)

                    if rowKey in seen or colKey in seen or squareKey in seen:
                        print(rowKey)
                        print(colKey)
                        print(squareKey)
                        return False
                    
                    seen.update([rowKey, colKey, squareKey])
        
        return True
                
                

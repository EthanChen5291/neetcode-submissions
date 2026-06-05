class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        indexMap = {}

        for row in range(len(board)):
            seen = set()
            for col in range(len(board)):
                num = board[row][col]

                if num != ".":
                    indexMap[f"{row}, {col}"] = num
                    
                    if num in seen:
                        return False
                    else:
                        seen.add(num)
        
        for col in range(len(board)):
            seen = set()
            for row in range(len(board)):
                num = board[row][col]

                if num != ".":
                    indexMap[f"{row}, {col}"] = num
                    
                    if num in seen:
                        return False
                    else:
                        seen.add(num)

        return self.verifySquares(indexMap)
    
    def verifySquares(self, indexMap: dict) -> bool:
        currentRow = 0
        currentCol = 0

        for i in range(9):
            seen = set()
            for row in range(3):
                for col in range(3):
                    r = currentRow+row
                    c = currentCol+col

                    if f"{r}, {c}" in indexMap: 
                        if indexMap[f"{r}, {c}"] in seen:
                            return False
                        else:
                            seen.add(indexMap[f"{r}, {c}"])
            
            if currentCol == 6:
                currentCol = 0
                currentRow += 3
            else:
                currentCol += 3
        
        return True
    
        

                

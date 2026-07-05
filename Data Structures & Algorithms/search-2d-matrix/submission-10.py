class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        left = 0
        right = rows * cols - 1

        while left <= right:
            middle = (left + right) // 2

            r = middle // cols
            c = middle % cols

            elt = matrix[r][c]

            if elt == target:
                return True
            elif elt < target:
                left = middle+1
            else:
                right = middle-1
        
        return False

            





        
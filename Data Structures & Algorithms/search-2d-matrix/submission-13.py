class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        maxRows = len(matrix)
        maxCols = len(matrix[0])
        
        left = 0
        right = (maxRows * maxCols) - 1

        while left <= right:
            mid = (left + right) // 2

            r, c = mid // maxCols, mid % maxCols

            if matrix[r][c] == target:
                return True
            elif target > matrix[r][c]:
                left = mid + 1
            else:
                right = mid - 1
        
        return False


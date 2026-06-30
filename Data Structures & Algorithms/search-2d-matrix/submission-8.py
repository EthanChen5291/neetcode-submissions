class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        targetRow = 0

        for i in range(rows):
            if matrix[i][0] <= target <= matrix[i][cols - 1]:
                targetRow = i
        
        left = 0
        right = cols - 1

        while left <= right:
            middle = (left + right) // 2

            elt = matrix[targetRow][middle]

            if elt < target:
                left = middle+1
            elif elt > target:
                right = middle-1
            else:
                return True
        
        return False
                



        
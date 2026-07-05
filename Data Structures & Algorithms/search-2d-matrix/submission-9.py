class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        #find correct row
        targetRow = -1

        left = 0
        right = rows-1

        while left <= right:
            middle = (left + right) // 2

            if matrix[middle][0] <= target <= matrix[middle][cols-1]:
                targetRow = middle
                break
            elif matrix[middle][0] > target:
                right = middle-1
            else:
                left = middle+1
        
        if targetRow == -1:
            return False

        left = 0
        right = cols-1
        
        while left <= right:
            middle = (left+right) // 2

            elt = matrix[targetRow][middle]

            if elt == target:
                return True
            elif elt < target:
                left = middle+1
            else:
                right = middle-1
        
        return False

            





        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        rowNum = 0

        for i in range(rows): # get correct row
            if matrix[i][0] <= target <= matrix[i][cols - 1]:
                rowNum = i
                break

        left = 0
        right = cols - 1

        while left <= right: # get correct row
            middle = (left + right) // 2
            elt = matrix[rowNum][middle]

            if elt < target:
                left = middle + 1
            elif elt == target:
                return True
            else:
                right = middle - 1

        
        return False
            
    
        



        
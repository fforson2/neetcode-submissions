class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #search row first to know the boundary
        ROWS = len(matrix)
        COLS = len(matrix[0])

        l, r = 0 , ROWS - 1

        while l <= r:

            mid = (l + r) // 2

            if target > matrix[mid][-1]:
                l = mid + 1

            elif target < matrix[mid][0]:
                r = mid - 1

            else:
                break

        if l > r:
            return False

        currentRow = mid
        l = 0
        r = COLS - 1

        while l <= r:
            mid = (l + r) // 2

            if target > matrix[currentRow][mid]:
                l = mid + 1

            elif target < matrix[currentRow][mid]:
                r = mid - 1

            else:
                return True

        return False










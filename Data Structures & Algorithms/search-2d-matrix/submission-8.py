class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        
        #Search rows
        l,r = 0, rows - 1

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

        #now mid is the place to search
        currentRow = mid
        l, r = 0, len(matrix[currentRow]) - 1

        while l <= r:
            mid = (l + r) // 2

            if target > matrix[currentRow][mid]:
                l = mid + 1

            elif target < matrix[currentRow][mid]:
                r = mid - 1

            else:
                return True

        return False











        

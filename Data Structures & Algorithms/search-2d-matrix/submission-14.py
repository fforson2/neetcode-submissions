class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #search rows to check the boundary the number falls within
        #search that particular ROW and find the number by doing
        #binary search


        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS - 1

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

        #search that particular ROW
        l, r = 0, COLS - 1
        currentR = mid

        while l <= r:
            mid = (l + r) // 2

            if target > matrix[currentR][mid]:
                l = mid + 1

            elif target < matrix[currentR][mid]:
                r = mid - 1

            else:
                return True

        return False






class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top , bottom = 0 , rows - 1

        while top <= bottom:
            currentRow = (top + bottom) // 2

            if target > matrix[currentRow][-1]:
                top = currentRow + 1

            elif target < matrix[currentRow][0]:
                bottom = currentRow - 1

            else:
                break

        # Edgecase check
        if not (top <= bottom):
            return False

        currentRow = (top + bottom) // 2
        
        l , r = 0 , cols - 1

        while l <= r:
            mid = (l + r) // 2

            if target > matrix[currentRow][mid]:
                l = mid + 1

            elif target < matrix[currentRow][mid]:
                r = mid - 1

            else:
                return True

        return False



        




        
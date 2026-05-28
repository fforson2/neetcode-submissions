class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix),len(matrix[0])

        top,bottom = 0,rows-1

        while top <= bottom:
            midR = (top+bottom)//2
            if target > matrix[midR][-1]:
                top = midR + 1
            elif target < matrix[midR][0]:
                bottom = midR - 1
            else: 
                break

        if not (top<=bottom):
            return False

        l,r = 0, cols-1
        row = (top+bottom)//2
        while l<=r:
            midC = (l+r)//2
            if target > matrix[row][midC]:
                l = midC + 1
            elif target < matrix[row][midC]:
                r = midC - 1
            else:
                return True
        return False

        
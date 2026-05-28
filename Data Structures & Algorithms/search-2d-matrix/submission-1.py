class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix), len(matrix[0])

        #Binary search on the row that contains our target

        topRow, bottomRow = 0, rows-1

        while topRow < bottomRow:
            mid = (topRow+bottomRow)//2

            #if the target is greater than the last element in the current row 
            #We update our topRow pointer to narrow down the search
            if target > matrix[mid][-1]:
                topRow = mid + 1
                #the exact opposite for the elif statement
            elif target < matrix[mid][0]:
                bottomRow = mid -1

            else:
                break
        #If our code excecuted the else because no target was found and as a result
        #Our topRow pointer was bigger than the bottomRow pointer
        #We immediately return False because target cannot be found in our array

        if not (topRow <= bottomRow):
            return False

        # Second binary search in the through each column of the selected row
        # To find the actual target

        l,r = 0, cols-1
        currentRow = (topRow + bottomRow)//2 # Row which contains the target

        while l<=r:
            midC = (l+r)//2

            if target > matrix[currentRow][midC]:
                l = midC + 1

            elif target < matrix[currentRow][midC]:
                r = midC -1

            else:
                return True

        return False


        
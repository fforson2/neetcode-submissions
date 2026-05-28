class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #create rows, cols, 3x3

        seen = set()

        for row in range(9):
            for col in range(9):

                val = board[row][col]

                if val == ".":
                    continue

                keys = [("col", col, val), ("row", row, val), ("3x3", row//3, col//3, val)]

                for key in keys:
                    if key in seen:
                        return False

                    seen.add(key)

        return True



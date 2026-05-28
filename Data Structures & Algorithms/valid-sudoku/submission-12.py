class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        seen = set()

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                keys = [("row",r, val),("col", c, val), ("3*3",r//3,c//3, val)]

                if val == ".":
                    continue

                for key in keys:
                    if key in seen:
                        return False

                    seen.add(key)

        return True
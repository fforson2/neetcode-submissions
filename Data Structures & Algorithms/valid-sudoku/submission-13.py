class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        seen = set()

        for r in range(9):
            for c in range(9):

                val = board[r][c]

                if val == ".":
                    continue

                keys = [('row', r, val), ('col', c, val), ('square', r//3, c//3, val)]


                for key in keys:
                    if key in seen:
                        return False

                    seen.add(key)

        return True



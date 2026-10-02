class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        pDiag = set() #(r + c)
        nDiag = set() #(r - c)
        col = set()
        res = []
        board = [["."] * n for i in range(n)]


        def backtrack(r):

            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                
                if (r + c) in pDiag or (r - c) in nDiag or c in col:
                    continue

                pDiag.add((r + c))
                nDiag.add((r - c))
                col.add(c)
                board[r][c] = "Q"
                
                backtrack(r + 1)
                pDiag.remove(r + c)
                nDiag.remove(r - c)
                col.remove(c)
                board[r][c] = "."

        backtrack(0)
        return res




                


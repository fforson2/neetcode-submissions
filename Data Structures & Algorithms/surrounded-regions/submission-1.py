class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS, COLS = len(board), len(board[0])

        # Mark border-connected O's as T's
        def capture(r, c):
            if (min(r,c) < 0 or r == ROWS or c == COLS 
            or board[r][c] != 'O'):
                return 

            board[r][c] = 'T'
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # Start DFS from border O's
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == 'O' and (r in [0, ROWS - 1] or c in [0, COLS - 1])):
                    capture(r, c)

        #  # Convert remaining O's to X's
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if board[r][c] == 'O':
        #             board[r][c] = 'X'

        # Convert protected T's back to O's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'

                elif board[r][c] == 'O':
                    board[r][c] = 'X'




class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        minH = [(grid[0][0], 0, 0)]
        visit = set()

        def addCell(r, c):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS
            or (r, c) in visit):
                return

            visit.add((r, c))
            heapq.heappush(minH, (grid[r][c], r, c))

        while minH:
            pos, r, c = heapq.heappop(minH)
            res = max(res, pos)
            if r == ROWS - 1 and c == COLS - 1:
                return res

            addCell( r + 1, c)
            addCell( r - 1, c)
            addCell(r, c + 1)
            addCell(r, c - 1)

        return res
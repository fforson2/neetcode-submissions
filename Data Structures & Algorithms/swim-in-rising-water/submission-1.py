class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        minH = [(grid[0][0], 0, 0)]
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        res = 0


        def addCell(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visited):
                return 

            visited.add((r, c))
            heapq.heappush(minH, (grid[r][c], r, c))


        while minH:
            pos, r, c = heapq.heappop(minH)
            res = max(res, pos)

            if r == ROWS - 1 and c == COLS - 1:
                return res

            addCell(r + 1, c)
            addCell(r - 1, c)
            addCell(r, c + 1)
            addCell(r, c - 1)

        return res






        

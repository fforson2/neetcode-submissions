class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        island = 0
        count = 0
        maxArea = 0

        def dfs (r, c):

            if (min(r, c) < 0 or (r,c) in visit or r >= ROWS or c >= COLS or
            grid[r][c] ==  0):
                return 0

            area = 1
            visit.add((r,c))
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)

            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visit:       
                    maxArea = max(maxArea, dfs(r,c))

        return maxArea


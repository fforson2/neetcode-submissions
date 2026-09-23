class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()

        def dfs(r, c):

            if (r, c) in visit:
                return 0

            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                return 1
            
            visit.add((r, c))

            perim = dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

            return perim


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    return dfs(r, c)

        
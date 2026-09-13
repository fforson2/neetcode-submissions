class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        island = 0

        def dfs(r, c, visit):
            if (min(r,c) < 0 or r >= ROWS or c >= COLS
            or (r,c) in visit or grid[r][c] == "0"):
                return

            visit.add((r,c))
            #explore other areas
            dfs(r + 1, c, visit)
            dfs(r - 1, c, visit)
            dfs(r, c - 1, visit)
            dfs(r, c + 1, visit)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    island += 1
                    dfs(r, c, visit)


        return island

            

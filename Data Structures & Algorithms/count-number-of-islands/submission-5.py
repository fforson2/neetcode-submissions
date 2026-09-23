class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        island = 0


        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c]   =="0"  or            (r, c) in visit:
                    return


            visit.add((r, c))
            neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in neighbors:
                dfs(r + dr, c + dc)


        for r in range(ROWS):
            for c in range(COLS):
                
                if grid[r][c] == "1" and (r, c) not in visit:
                    island += 1
                    dfs(r, c)

        return island





            
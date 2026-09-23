class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        maxArea = 0
 

        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0 or (r, c) in visit:
                return 0

            area = 1
            visit.add((r, c))
            neighbours = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in neighbours:
                area += dfs(r + dr, c + dc)

            return area

        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == 1 and (r, c) not in visit:
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea




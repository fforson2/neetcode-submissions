class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        q = deque()
        fresh, time = 0, 0

        def addCell(r, c):
            nonlocal fresh
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] != 1 or (r, c) in visit:
                return

            #adding fresh fruits to the queue
            q.append((r, c))
            visit.add((r, c))
            fresh -= 1

        #building phase
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))

        #rotting of fresh fruits and keeping track of time
        time = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                addCell (r + 1, c)
                addCell (r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)

            time += 1

        return time if fresh == 0 else -1



                
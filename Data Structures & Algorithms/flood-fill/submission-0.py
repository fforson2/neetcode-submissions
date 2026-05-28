class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        ROWS, COLS = len(image), len(image[0])
        visit = set()

        original = image[sr][sc]
        if original == color:
            return image

        def dfs(r, c):
            # Base cases (same structure as your template)
            if (min(r, c) < 0 or
                r == ROWS or c == COLS or
                (r, c) in visit or
                image[r][c] != original):
                return

            # Mark visited
            visit.add((r, c))

            # Change color
            image[r][c] = color

            # Explore 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c) 
            dfs(r, c + 1)
            dfs(r, c - 1)

            # (No need to remove from visit for flood fill)

        dfs(sr, sc)
        return image
        


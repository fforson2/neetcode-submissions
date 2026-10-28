class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        #build ajacency list
        adj = {}
        N = len(points)
        for i in range(N):
            adj[i] = []

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                distance = abs(x1-x2) + abs(y1-y2)
                adj[i].append((distance, j))
                adj[j].append((distance, i))

        
        minH = [(0, 0)] #dist, node
        res = 0
        visited = set()

        while len(visited) < N:
            dist, n1 = heapq.heappop(minH)
            if n1 in visited:
                continue
            res += dist
            visited.add((n1))

            for distance, n2 in adj[n1]:
                heapq.heappush(minH, (distance, n2))

        return res







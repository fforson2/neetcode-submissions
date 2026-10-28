class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        minH = [(0, k)] #time, target
        graph = defaultdict(list)
        visited = set()

        for src, dst, time in times:
            graph[src].append((time, dst))

        while minH:
            t1, n1 = heapq.heappop(minH)
            if n1 in visited:
                continue
            visited.add(n1)
            arrival = t1

            for t2, n2 in graph[n1]:
                heapq.heappush(minH, (t1 + t2, n2))

        return arrival if len(visited) == n else -1

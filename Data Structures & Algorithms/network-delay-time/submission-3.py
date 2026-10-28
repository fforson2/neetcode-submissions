class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        arrival = 0
        minHeap = [(0, k)] #time, dst
        visited = set()

        graph = defaultdict(list)

        for src, dst, time in times:
            graph[src].append([time, dst])

        while minHeap:
            t1, n1 = heapq.heappop(minHeap)

            if n1 in visited:
                continue
            visited.add(n1)
            arrival = t1

            for t2, n2 in graph[n1]:
                heapq.heappush(minHeap, [t1 + t2, n2])
        
        return arrival if len(visited) == n else -1
    
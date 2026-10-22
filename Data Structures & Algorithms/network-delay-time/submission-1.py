class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)

        for src, target, travel_time in times:
            graph[src].append((target, travel_time))

        heap = [(0, k)]

        visited = set()
        answer = 0

        while heap:
            arrival, node = heapq.heappop(heap)
            if node in visited:
                continue

            visited.add(node)
            answer = arrival

            for nei, travel_time in graph[node]:
                if nei not in visited:
                    heapq.heappush(heap, (arrival + travel_time, nei))

            if len(visited) == n:
                return answer

        return -1
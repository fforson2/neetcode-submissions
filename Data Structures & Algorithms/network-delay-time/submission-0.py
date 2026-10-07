class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        #building the adj list
        adj = {}

        for i in range(1, n + 1):
            adj[i] = []

        for src, dst, time in times:
            adj[src].append([dst, time])


        minHeap = [(0, k)] #time, destination
        shortest = {}

        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue

            shortest[n1] = t1

            #go through the neighbours
            for n2, t2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, (t1 + t2, n2))

        if len(shortest) != n:
            return -1

        return max(shortest.values())





        


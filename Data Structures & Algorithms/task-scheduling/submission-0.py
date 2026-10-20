class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        #count all elements and store in a max heap
        countMap = {}
        heap = []

        for task in tasks:
            countMap[task] = 1 + countMap.get(task, 0)

        for val in countMap.values():
            heapq.heappush(heap, -val)

        q = deque() # [cnt, time]
        time = 0

        while q or heap:
            time += 1

            if heap:
                count = heapq.heappop(heap)
                val = count + 1

                if val:
                    q.append([val, time + n])

            if q and q[0][1] == time:
                count = q.popleft()[0]
                heapq.heappush(heap, count)

        return time

        
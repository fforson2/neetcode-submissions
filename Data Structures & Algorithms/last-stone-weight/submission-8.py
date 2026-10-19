class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            if y > x:
                val = y-x
                heapq.heappush(heap, -val)

        return abs(heap[0]) if heap else 0
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        #loop through the points
        #calculate their distances
        #store in a heap (dis, [cor])
        #use a min heap and pop according to k and add the result to a list

        heap = []
        res = []
        for x1, x2 in points:
            dst = math.sqrt(x1**2 + x2**2)
            heapq.heappush(heap, (dst, [x1, x2]))

        while k and heap:
            k -= 1
            dst, cor = heapq.heappop(heap)
            res.append(cor)

        return res

        
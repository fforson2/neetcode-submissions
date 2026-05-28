import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        #maxHeap
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)

        while k > 0:
            richest = heapq.heappop(gifts)
            heapq.heappush(gifts, -(math.floor(math.sqrt(abs(richest)))))
            k -= 1

        return abs(sum(gifts))
        
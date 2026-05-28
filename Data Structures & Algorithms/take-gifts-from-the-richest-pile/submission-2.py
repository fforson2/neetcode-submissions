import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        gifts = [-g for g in gifts]
        heapq.heapify(gifts)

        for i in range(k):
            val = math.floor(math.sqrt(abs(heapq.heappop(gifts))))
            heapq.heappush(gifts, -val)

        return -sum(gifts)

        
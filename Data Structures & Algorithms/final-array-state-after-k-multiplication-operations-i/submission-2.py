class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        res = nums[:]
        heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)


        for i in range(k):
            num, ind = heapq.heappop(heap)
            res[ind] = multiplier * num
            heapq.heappush(heap, (multiplier * num, ind))

        return res
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        heap = [(num, i) for i, num in enumerate(nums)]
        res = nums[:]
        heapq.heapify(heap)

        while k > 0:
            newNum, ind = heapq.heappop(heap)
            res[ind] = newNum * multiplier
            heapq.heappush(heap, (newNum * multiplier, ind))
            k -= 1

        return res


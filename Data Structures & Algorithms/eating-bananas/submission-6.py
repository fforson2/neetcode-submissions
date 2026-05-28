class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1 , max(piles)
        k = r

        while l <= r:
            totalHours = 0
            res = (l + r) // 2
            
            for p in piles:
                totalHours += math.ceil(p/res)

            if totalHours <= h:
                k = min(k , res)
                r = res - 1

            else:
                l = res + 1

        return k





        
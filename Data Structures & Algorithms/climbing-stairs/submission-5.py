class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp1, dp2 = 0, 1

        for i in range(n ):
            tmp = dp2
            dp2 = dp1 + dp2
            dp1 = tmp

        return dp2

            
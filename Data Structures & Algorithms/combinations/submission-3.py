class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        curComb, combs = [], []

        def helper(i, curComb, combs):
            if len(curComb) == k:
                combs.append(curComb.copy())
                return

            if i > n:
                return

            for j in range(i, n+1):
                curComb.append(j)
                helper(j+1, curComb, combs)
                curComb.pop()
            
        helper(1, curComb, combs)

        return combs
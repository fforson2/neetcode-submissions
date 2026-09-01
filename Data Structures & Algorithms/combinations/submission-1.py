class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        curComb, combs = [], []

        def helper(i, curComb, combs, n, k):
            if len(curComb) == k:
                combs.append(curComb.copy())
                return

            if i > n:
                return


            curComb.append(i)
            helper(i+1, curComb, combs, n, k)
            curComb.pop()
            helper(i+1, curComb, combs, n, k)


        helper(1, curComb, combs, n, k)

        return combs
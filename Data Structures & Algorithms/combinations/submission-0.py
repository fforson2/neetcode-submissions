class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curComb, comb = [], []

        def helper(i, curComb, n, k):
            if len(curComb) == k:
                comb.append(curComb.copy())
                return 

            if i > n:
                return

            curComb.append(i)
            helper(i + 1, curComb, n, k)
            curComb.pop()
            helper(i + 1, curComb, n, k)


        helper(1, curComb, n , k)

        return comb

        
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res, comb = [], []
        candidates.sort()

        def helper(i, comb, candidates):
            curSum = sum(comb)
            if target == curSum:
                res.append(comb.copy())
                return

            if i >= len(candidates) or curSum > target:
                return

            comb.append(candidates[i])
            helper(i + 1, comb, candidates)
            comb.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            helper(i + 1, comb, candidates)

        helper(0, comb, candidates)

        return res
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        curComb, combs = [], []

        def dfs(i, curComb, combs):
            if sum(curComb) == target:
                combs.append(curComb.copy())
                return

            if i == len(candidates) or sum(curComb) > target:
                return

            curComb.append(candidates[i])
            dfs(i + 1, curComb, combs)
            curComb.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curComb, combs)

        dfs(0, curComb, combs)

        return combs
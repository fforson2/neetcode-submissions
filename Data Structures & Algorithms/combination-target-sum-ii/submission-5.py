class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        curSum = 0
        curComb, comb = [], []
        candidates.sort()


        def helper(i, curComb, comb, candidates):

            curSum = sum(curComb)
            if curSum == target:
                comb.append(curComb.copy())
                return 

            if i == len(candidates) or curSum > target:
                return 

            curComb.append(candidates[i])
            helper(i + 1, curComb, comb, candidates)
            curComb.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            helper(i + 1, curComb, comb, candidates)

        helper(0, curComb, comb, candidates)

        return comb


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        curComb, combs = [], []

        def dfs(i, curComb, combs):
            if sum(curComb) == target:
                combs.append(curComb.copy())
                return

            if i == len(nums) or sum(curComb) > target:
                return

            curComb.append(nums[i])
            dfs(i, curComb, combs)
            curComb.pop()
            dfs(i + 1, curComb, combs)

        dfs(0, curComb, combs)
        return combs
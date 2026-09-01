class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        curComb, combs = [], []

        def helper(i, curComb, combs, nums):
            
            if sum(curComb) == target:
                combs.append(curComb.copy())
                return
            if i == len(nums) or sum(curComb) > target:
                return

            curComb.append(nums[i])
            helper(i, curComb, combs, nums)
            curComb.pop()
            helper(i + 1, curComb, combs, nums)

        helper(0, curComb, combs, nums)

        return combs
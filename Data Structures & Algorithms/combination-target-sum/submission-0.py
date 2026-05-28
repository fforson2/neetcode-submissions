class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        #approach as a subset 
        #modify to keep track of total of each subset
        #add when total == target
        
        res, comb = [], []

        def helper(i, comb, nums):
            curSum = sum(comb)
            if target == curSum:
                res.append(comb.copy())
                return

            if i >= len(nums) or curSum > target:
                return

            comb.append(nums[i])
            helper(i, comb, nums)
            comb.pop()
            helper(i + 1, comb, nums)

        helper(0, comb, nums)

        return res
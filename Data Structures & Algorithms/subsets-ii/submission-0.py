class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []
        nums.sort()

        def helper(i, subset, nums):

            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            helper(i + 1, subset, nums)
            

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            subset.pop()

            helper(i + 1, subset, nums)

        helper(0, subset, nums)

        return res


        
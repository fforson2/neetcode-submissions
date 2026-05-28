class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        curSet, subSet = [], []

        def helper(i, curSet, subSet, nums):
            if i == len(nums):
                subSet.append(curSet.copy())
                return 

            curSet.append(nums[i])
            helper(i + 1, curSet, subSet, nums)
            curSet.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            helper(i + 1, curSet, subSet, nums)

        helper(0, curSet, subSet, nums)

        return subSet
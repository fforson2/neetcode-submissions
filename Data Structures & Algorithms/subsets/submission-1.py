class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        curSet, subSet = [], []

        def helper (i, curSet, subSet, nums):
            if i == len(nums):
                subSet.append(curSet.copy())
                return

            curSet.append(nums[i])
            helper(i + 1, curSet, subSet, nums)

            curSet.pop()
            helper(i + 1, curSet, subSet, nums)


        helper(0, curSet, subSet, nums)
        return subSet
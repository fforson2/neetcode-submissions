class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def helper(i, nums):
            if i == len(nums):
                return [[]]

            perms = helper(i + 1, nums)
            res = []

            for p in perms:
                for j in range(len(p) + 1):
                    newPerm = p.copy()
                    newPerm.insert(j, nums[i])
                    res.append(newPerm)

            return res

        return helper(0, nums)
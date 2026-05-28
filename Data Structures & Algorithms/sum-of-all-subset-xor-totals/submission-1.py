class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subSet = []
        self.total = 0

        def helper(i, subSet, nums):

            if i >= len(nums):
                currentXor = 0
                for val in subSet:
                    currentXor ^= val
                self.total += currentXor
                return

            subSet.append(nums[i])
            helper(i + 1, subSet, nums)
            subSet.pop()
            helper(i + 1, subSet, nums)

        helper(0, subSet, nums)
        return self.total
        
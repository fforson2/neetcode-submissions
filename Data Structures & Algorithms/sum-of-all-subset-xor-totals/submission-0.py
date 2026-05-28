class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        #first find all subset
        subset = []
        self.total = 0

        def helper(i, subset):
            if i >= len(nums):
                #find the xor here and store in a variable
                current_xor = 0
                for val in subset:
                    current_xor ^= val
                self.total += current_xor
                return

            subset.append(nums[i])
            helper(i + 1, subset)
            subset.pop()
            helper(i + 1, subset)

        helper(0, subset)
        return self.total

        
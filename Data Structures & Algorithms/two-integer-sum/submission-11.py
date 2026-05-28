class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexTracker = {}

        for i,n in enumerate(nums):
            diff = target - n

            if diff in indexTracker:
                return [indexTracker[diff],i]

            indexTracker[n] = i
        
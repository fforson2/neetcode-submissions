class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        countMap = {}

        for i,a in enumerate(nums):
            diff = target - a

            if diff in countMap:
                return [countMap[diff], i]

            countMap[a] = i

        
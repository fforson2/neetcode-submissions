class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        countMap = {}

        for num in nums:
            countMap[num] = 1 + countMap.get(num,0)

        for val in countMap.values():
            if val >= 2:
                return True

        return False
         
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 != 0:
            return False

        dp = {0}
        target = sum(nums) / 2

        for i in range(len(nums)):
            newDp = set()
            for num in dp:
                newDp.add(num + nums[i])
                newDp.add(num)

                if (num + nums[i]) == target:
                    return True

            dp = newDp

        return False

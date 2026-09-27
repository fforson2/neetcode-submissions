class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        curMin, curMax = 1, 1
        maxP = max(nums)

        for num in nums:

            temp = curMax * num
            curMax = max(temp, curMin * num, num)
            curMin = min(temp, curMin * num , num)

            maxP = max(curMax, maxP)

        return maxP
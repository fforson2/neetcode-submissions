class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # for num in nums:
        #     index = abs(num) - 1

        #     if nums[index] > 0:
        #         nums[index] = -nums[index]

        #     else:
        #         return abs(num)


        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
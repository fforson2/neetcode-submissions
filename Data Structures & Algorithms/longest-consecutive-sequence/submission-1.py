class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longestStreak = 0

        for n in nums:
            if (n-1) not in nums:
                length = 1

                while (n+length) in nums:
                    length += 1
                longestStreak = max(longestStreak,length)

        return longestStreak
                
        
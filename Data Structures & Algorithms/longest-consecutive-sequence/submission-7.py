class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        maxLength, length = 0, 0

        for num in nums:
            if (num - 1) not in nums:
                length = 1

                while length + num in nums:
                    length += 1

                maxLength = max(maxLength, length)

        return maxLength
                
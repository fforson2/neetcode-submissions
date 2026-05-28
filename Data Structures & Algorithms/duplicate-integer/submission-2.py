class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        count ={}

        for number in nums:
            if number in count:
                count[number] += 1
            else:
                count[number] = 1

        for k in count:
            if count[k] >= 2:
                return True                          
        return False 
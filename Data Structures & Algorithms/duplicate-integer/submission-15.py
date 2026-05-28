class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        myList = []

        for num in nums:
            
            if num in myList:
                return True

            myList.append(num)

        return False

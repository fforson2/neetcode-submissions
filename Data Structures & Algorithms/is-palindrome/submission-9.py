class Solution:
    def isPalindrome(self, s: str) -> bool:

        myList = []

        for char in s:
            if char.isalnum():
                myList.append(char.lower())

        l,r = 0, len(myList) - 1

        while l <= r:
            if myList[l] != myList[r]:
                return False
            l += 1
            r -= 1
        return True
        
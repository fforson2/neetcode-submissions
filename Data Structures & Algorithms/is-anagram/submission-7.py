class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        countMap = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char in countMap:
                countMap[char] +=1
            else:
                countMap[char] = 1

        for char in t:
            if char in countMap:
                countMap[char] -= 1
            else:
                countMap[char]= 1

        for k in countMap:
            if countMap[k]!=0:
                return False
        return True    
                                                



        
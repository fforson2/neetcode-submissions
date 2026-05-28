class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        countMap = {}

        for char in s:
            countMap[char] = 1 + countMap.get(char, 0)

        for char in t:
            if char not in countMap:
                return False

            countMap[char] -= 1


        for val in countMap.values():
            if val < 0:
                return False

        return True
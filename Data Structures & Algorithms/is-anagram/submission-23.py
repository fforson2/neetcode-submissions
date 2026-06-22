class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        countToMap = {}

        for char in s:
            countToMap[char] = 1 + countToMap.get(char, 0)

        for char in t:
            if char not in countToMap:
                return False

            countToMap[char] -= 1

        for val in countToMap.values():
            if val < 0:
                return False

        return True
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Edgecase

        if len(s) != len(t):
            return False

        countMap = {}

        for char in s:
            countMap[char] = 1 + countMap.get(char, 0)

        for char in t:
            if char not in countMap:
                return False

            countMap[char] -= 1

            if countMap[char] < 0:
                return False

        return True
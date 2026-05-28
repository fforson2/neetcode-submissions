class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        ### sorting method

        return sorted(s)== sorted(t)
        
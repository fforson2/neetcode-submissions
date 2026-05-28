class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        l, r = 0, 1
        length = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            length = max(length, r - l + 1)

            seen.add(s[r])

        return length


        
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        countMap = {}
        maxLength = 0

        for r in range(len(s)):
            countMap[s[r]] = 1 + countMap.get(s[r], 0)

            if (r - l + 1) - max(countMap.values()) <= k:
                maxLength = max(maxLength, r - l + 1)

            else:
                countMap[s[l]] -= 1
                l += 1

        return maxLength

            


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        countMap = {}
        maxLength, maxF = 0, 0

        for r in range(len(s)):
            countMap[s[r]] = 1 + countMap.get(s[r], 0)
            maxF = max(maxF, max(countMap.values()))

            if (r - l + 1) - maxF > k:
                countMap[s[l]] -= 1
                l += 1
            maxLength = max(maxLength, r - l + 1)


        return maxLength

            


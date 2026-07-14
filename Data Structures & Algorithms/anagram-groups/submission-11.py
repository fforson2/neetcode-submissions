class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        
        for word in strs:
            res = [0] * 26

            for char in word:
                res[ord(char) - ord("a")] += 1

            key = tuple(res)

            if key not in result:
                result[key] = []

            result[key].append(word)

        return list(result.values())



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list)
        
        for word in strs:
            countMap = [0]*26

            for char in word:
                countMap[ord(char)-ord('a')]+=1
            result[tuple(countMap)].append(word)

        return list(result.values())


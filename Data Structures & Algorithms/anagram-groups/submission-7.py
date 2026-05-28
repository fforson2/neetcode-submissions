class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countMap = {} #key(tuple) val (list of words)

        for word in strs:
            rep = [0] * 26

            #Build this list

            for char in word:
                rep[ord(char) - ord("a")] += 1
            key = tuple(rep)
            if key not in countMap:
                countMap[key] = [word]

            else:
                countMap[key] += [word]

            
        return list(countMap.values())

            

        
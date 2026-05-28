class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        count = 0

        for i in range(len(words)):
            L = len(pref)
            w1 = words[i]


            if pref == w1[:L]:
                count +=1

        return count
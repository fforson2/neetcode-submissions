class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j+=1
            lengthOfWord = int(s[i:j])
            
            result.append(s[j+1:j+1+lengthOfWord])
            i = j + 1 + lengthOfWord

        return result



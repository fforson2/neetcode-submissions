class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:

        res = []

        i,j = 0, 0

        while i < len(s):
            
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            start = j + 1
            end = start + length

            res.append(s[start:end])
            
            i, j = end, end


        return res

            

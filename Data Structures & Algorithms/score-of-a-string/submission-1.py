class Solution:
    def scoreOfString(self, s: str) -> int:

        
        total = 0
    
        for i in range(1,len(s)):
            total += abs(ord(s[i-1]) - ord(s[i]))

        return total
        # lists = []
        # for char in s:
        #     val = ord(char) 
        #     lists.append(val)

        # for i in range(1, len(lists)):
        #     total += abs(lists[i-1] - lists[i])

        # return total
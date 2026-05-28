class Solution:
    def scoreOfString(self, s: str) -> int:

        lists = []
        total = 0
        
        for char in s:
            val = ord(char) 
            lists.append(val)

        for i in range(1, len(lists)):
            total += abs(lists[i-1] - lists[i])

        return total

        
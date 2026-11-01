class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = []

        def count(num):
            counter = 0
            while num > 0:
                if num & 1 == 1:
                    counter += 1
                num = num >> 1
            return counter

        for i in range(n + 1):
            res.append(count(i))

        return res
        
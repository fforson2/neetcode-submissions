class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res, newPerm = [], []
        countMap = {}

        for num in nums:
            countMap[num] = 1 + countMap.get(num, 0)


        def dfs():
            if len(newPerm) == len(nums):
                res.append(newPerm.copy())
                return 

            for n in countMap:
                if countMap[n] > 0:
                    newPerm.append(n)
                    countMap[n] -= 1

                    dfs()
                    countMap[n] += 1
                    newPerm.pop()
        dfs()
        return res


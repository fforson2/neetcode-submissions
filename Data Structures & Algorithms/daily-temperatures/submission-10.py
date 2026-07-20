class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = [] #(index, temperature)

        for ind,temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                stackInd, stackTemp = stack.pop()
                res[stackInd] = ind - stackInd

            stack.append((ind, temp))

        return res
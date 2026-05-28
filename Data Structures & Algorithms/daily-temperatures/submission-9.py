class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = [] #(temp, index)


        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                stackTemp, stackInd = stack.pop()
                res[stackInd] = i - stackInd

            stack.append((temperatures[i], i))

        return res
        
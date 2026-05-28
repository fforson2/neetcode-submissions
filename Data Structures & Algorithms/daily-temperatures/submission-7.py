class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [] #temperature, index
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                prevTemp = stack.pop()
                res[prevTemp[1]] = i - prevTemp[1]

            stack.append([temperatures[i], i])

        return res
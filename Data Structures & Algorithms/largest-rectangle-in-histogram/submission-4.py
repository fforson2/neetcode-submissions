class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = [] # (index, height)
        maxArea = 0

        for i,h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()

                #setting key variables after popping
                start = index
                width = i - index
                maxArea = max(maxArea, width*height)

            stack.append((start,h))

        for i,h in stack:

            width = len(heights) - i
            maxArea = max(maxArea, width * h)

        return maxArea
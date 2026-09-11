class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        
        def helper(openN, closedN):
            #valid parenthesis
            if openN == closedN == n:
                res.append("".join(stack))
                return

            #adding open parenthesis if openN < n
            if openN < n:
                stack.append('(')
                helper(openN + 1, closedN)
                stack.pop()

            #adding closed parenthese if close < open
            if closedN < openN:
                stack.append(')')
                helper(openN, closedN + 1)
                stack.pop()

        helper(0, 0)
        return res



class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)

        #minStack
        if self.minStack:
            if self.minStack[-1] < val:
                val = self.minStack[-1]
       
        self.minStack.append(val)
        

    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]

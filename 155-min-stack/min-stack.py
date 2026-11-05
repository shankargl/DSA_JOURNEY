class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, value: int) -> None:
        mini=self.getMin()
        if mini is None or mini>value:
            mini=value
        self.stack.append([value,mini])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None
        

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
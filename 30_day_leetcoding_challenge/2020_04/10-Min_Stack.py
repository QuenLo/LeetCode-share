class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.LL = []
        self.min_LL = []
        

    def push(self, x: int) -> None:
        self.LL.append( x )
        if len( self.min_LL ) == 0 or x <= self.min_LL[-1]:
            self.min_LL.append( x )

    def pop(self) -> None:
        if self.LL[-1] == self.min_LL[-1]:
            self.min_LL.pop()
        self.LL.pop()

    def top(self) -> int:
        return self.LL[ -1 ]

    def getMin(self) -> int:
        return self.min_LL[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

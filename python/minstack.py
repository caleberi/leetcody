class MinStack:

    def __init__(self):
        self.stk = []
        self.min = []

    # [null,null,null,null,-3,null,0,-2]
    def push(self, val: int) -> None:
        if len(self.min) and val < self.min[-1]:
            self.min.append(val)
        if not len(self.min):
            self.min.append(val)
        self.stk.append(val) # add to stack [ 1,3,4,8] <- (9) = > [ 1,3,4,8,9]

    def pop(self) -> None:
        if len(self.stk) and len(self.min) and self.stk[-1] == self.min[-1]:
            self.min.pop()
        if len(self.stk):   
            self.stk.pop()

    def top(self) -> int:
        if not len(self.stk):
            return -100000
        return self.stk[-1]

    def getMin(self) -> int:
        if not len(self.stk):
            return -100000
        return self.min[-1]
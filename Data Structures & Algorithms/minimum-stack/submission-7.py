class MinStack:

    def __init__(self):
        self.stack = [] 
        self.minimums = []
        self.currMin = None

    def push(self, val: int) -> None:
        if not self.minimums:
            self.currMin = val
        else:
            self.currMin = min(self.currMin, val)
        
        self.stack.append(val)
        self.minimums.append(self.currMin)

        return

    def pop(self) -> None:
        self.stack.pop()
        self.minimums.pop()

        if self.minimums:
            self.currMin = self.minimums[-1]
        else:
            self.currMin = None

        return
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimums[-1]
        

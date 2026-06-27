class MinStack:

    def __init__(self):
        self.stack = []
        self.minimums = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minimums:
            self.minimums.append(val)
        else:
            currentMin = self.minimums[-1]
            self.minimums.append(min(currentMin, val))
        
        return

    def pop(self) -> None:
        self.stack.pop()
        self.minimums.pop()

        return

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimums[-1]

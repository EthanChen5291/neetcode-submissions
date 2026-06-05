from typing import Optional

class Node:
    def __init__(self, val: int, min_val: int, next_node: Optional[Node] = None):
        self.val = val
        self.min_val = min_val
        self.next = next_node

class MinStack:

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if not self.head:
            self.head = Node(val, val)
            return
        
        current_min = min(self.head.min_val, val)
        self.head = Node(val, current_min, self.head)
        return

    def pop(self) -> None:
        if not self.head:
            return 

        self.head = self.head.next


    def top(self) -> int:
        if not self.head:
            return -1

        return self.head.val
        

    def getMin(self) -> int:
        if self.head:
            return self.head.min_val
        else:
            return -1
        

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return

        copy = Node(0, None)

        curr = head
        nodeMap = {}

        copyCurr = copy

        while curr:
            copyCurr.val = curr.val

            if curr.next:
                node = Node(0, None)
                copyCurr.next = node

            nodeMap[curr] = copyCurr

            curr = curr.next
            copyCurr = copyCurr.next
        
        curr = head

        while curr: # figure out random indicies
            if curr.random:
                nodeMap[curr].random = nodeMap[curr.random]
            
            curr = curr.next
        
        return copy

        
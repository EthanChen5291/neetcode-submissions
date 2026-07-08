# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        return self.cycleHelper(head.next, head)

    def cycleHelper(self, fast: Optional[ListNode], slow: Optional[ListNode]) -> bool:
        if fast == slow:
            return True

        if not fast or not fast.next:
            return False
            
        return self.cycleHelper(fast.next.next, slow.next)
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def helper(n1: Optional[ListNode], n2: Optional[ListNode], carry: int):
            if not n1 and not n2 and not carry:
                return None
            
            total = carry
            if n1:
                total += n1.val
            if n2:
                total += n2.val
            
            node = ListNode(total % 10)
            node.next = helper(
                n1.next if n1 else None,
                n2.next if n2 else None,
                total // 10
            )
            return node

        return helper(l1, l2, 0)
            



            
            
        
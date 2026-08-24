# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add(n1: Optional[ListNode], n2: Optional[ListNode], carry: int) -> Optional[ListNode]:
            if not n1 and not n2 and not carry:
                return None
            
            total = carry

            if n1:
                total += n1.val
                n1 = n1.next
            if n2:
                total += n2.val
                n2 = n2.next

            res = ListNode(total % 10)
            res.next = add(n1, n2, total // 10)
            return res

        return add(l1, l2, 0)




            
            
        
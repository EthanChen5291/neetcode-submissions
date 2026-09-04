# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseHelper(node: Optional[ListNode], prev: Optional[ListNode]):
            if not node:
                return prev
            
            temp = node.next
            node.next = prev
            
            return reverseHelper(temp, node)
        
        return reverseHelper(head, None)

            

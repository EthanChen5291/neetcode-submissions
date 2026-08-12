# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2

        digits = []

        while curr1 and curr2:
            total = curr1.val + curr2.val
            digits.append(total)

            curr1 = curr1.next
            curr2 = curr2.next


        while curr1:
            digits.append(curr1.val)
            curr1 = curr1.next
        
        while curr2:
            digits.append(curr2.val)
            curr2 = curr2.next
        
        # iterate through array 

        res = ListNode(0)
        node = res

        for i, n in enumerate(digits):
            if n >= 10: 
                n -= 10
                
                if i+1 < len(digits):
                    digits[i+1] += 1
                else:
                    digits.append(1)
            
            node.val = n

            if i+1 < len(digits):
                new = ListNode(0)
                node.next = new
                node = node.next
            
        return res

            
            

            


            
            
        
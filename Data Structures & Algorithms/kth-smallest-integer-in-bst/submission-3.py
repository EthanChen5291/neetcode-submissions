# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # go all the way to the left
        # when left is invalid, backtrack up once
        # check out middle, then check out right
        n = 0

        def inorder(curr):
            nonlocal n 
            
            if not curr:
                return -1

            left = inorder(curr.left)

            if left >= 0:
                return left

            n += 1

            if n == k:
                return curr.val

            if curr:
                right = inorder(curr.right)

                if right >= 0:
                    return right
            
            return -1
        
        return inorder(root)
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # do bfa to find height of res

        # height -> num of nodes above it < k but including it, > k
        count = 0
        res = None

        def inorder(node: Optional[TreeNode]) -> int:
            nonlocal count
            nonlocal res

            if not node:
                return None
            
            left = inorder(node.left)
            count += 1

            if count == k:
                res = node.val
            
            right = inorder(node.right)

        inorder(root)
        return res




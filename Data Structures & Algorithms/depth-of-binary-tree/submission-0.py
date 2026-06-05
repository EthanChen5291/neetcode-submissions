# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxLen(root: Optional[TreeNode]) -> height:
            if not root:
                return 0

            return 1 + max(maxLen(root.left), maxLen(root.right))
        
        return maxLen(root)
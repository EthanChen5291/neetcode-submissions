# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def height(root: Optional[TreeNode]) -> int:
            nonlocal diameter

            if not root:
                return 0

            leftLen = height(root.left)
            rightLen = height(root.right)

            diameter = max(diameter, leftLen + rightLen)

            return 1 + max(leftLen, rightLen)
        
        height(root)
        return diameter
        
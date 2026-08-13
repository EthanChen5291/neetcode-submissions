# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftMaxLen = 1 + self.maxDepth(root.left)
        rightMaxLen = 1 + self.maxDepth(root.right)

        maxLen = max(leftMaxLen, rightMaxLen)

        return maxLen
             


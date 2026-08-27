# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def helper(left: int, node: Optional[TreeNode], right: int) -> bool:
            if not node:
                return True

            if left < node.val < right:
                left = helper(left, node.left, node.val)
                right = helper(node.val, node.right, right)

                return left and right
            
            return False
        

        return helper(float("-inf"), root, float("inf"))

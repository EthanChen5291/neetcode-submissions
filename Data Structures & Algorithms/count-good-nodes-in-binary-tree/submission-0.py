# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfa
        # maintain highest val prior

        def nodeHelper(node: TreeNode, highest: int) -> int:
            if not node:
                return 0

            if node.val >= highest:
                leftCount = nodeHelper(node.left, node.val)
                rightCount = nodeHelper(node.right, node.val)

                return 1 + leftCount + rightCount
            else:
                leftCount = nodeHelper(node.left, highest)
                rightCount = nodeHelper(node.right, highest)

                return leftCount + rightCount
            
        return nodeHelper(root, root.val)




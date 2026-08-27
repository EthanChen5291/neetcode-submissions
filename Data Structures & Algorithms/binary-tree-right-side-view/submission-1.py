# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        # a node is visible if nothing to its right exists
        # only 1 per height

        # bfa with the rightmost node added to the list every time

        queue = []
        res = []

        queue.append(root)

        while queue:
            currRes = []

            l = len(queue)
            for i in range(l):
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                currRes.append(node.val)
            
            res.append(currRes.pop())
        
        return res





                
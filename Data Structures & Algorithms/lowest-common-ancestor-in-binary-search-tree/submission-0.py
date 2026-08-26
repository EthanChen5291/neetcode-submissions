# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def sameTree(p: Optional[TreeNode], q: Optional[TreeNode]):
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            return sameTree(p.left, q.left) and sameTree(p.right, q.right)
        
        def isSubtree(head: Optional[TreeNode], sub: Optional[TreeNode]):
            if not head:
                return False
            
            if sameTree(head, sub):
                return True
            
            return isSubtree(head.left, sub) or isSubtree(head.right, sub)
        
        if not root:
            return None
        
        if isSubtree(root, p) and isSubtree(root, q):
            left = self.lowestCommonAncestor(root.left, p, q)

            if left:
                return left
            
            right = self.lowestCommonAncestor(root.right, p, q)

            if right:
                return right
            
            return root
        
        return None
        

        
        
        # lca only if p and q reachable from res

        # subtree check on every node, tracking most recent
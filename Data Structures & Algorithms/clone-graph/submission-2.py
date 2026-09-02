"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # undirected -> double edges. do i have to deal with it?
        if not node:
            return None

        oldMap = {}

        def dfs(old) -> None:
            if old in oldMap:
                return oldMap[old]
            
            new = Node(old.val)
            oldMap[old] = new

            for neighbor in old.neighbors:
                newNeighbor = dfs(neighbor)
                new.neighbors.append(newNeighbor)
            
            return new
        
        return dfs(node)
                




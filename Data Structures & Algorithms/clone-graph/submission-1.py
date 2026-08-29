"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def clone(oldHead: Optional['Node'], oldMap: dict) -> Optional['Node']:
            if oldHead in oldMap:
                return oldMap[oldHead]
            
            if not oldHead:
                return None
            
            newNode = Node(oldHead.val)
            oldMap[oldHead] = newNode
            
            for neighbor in oldHead.neighbors:
                newNeighbor = clone(neighbor, oldMap)

                if not newNode.neighbors:
                    newNode.neighbors = []
                
                newNode.neighbors.append(newNeighbor)
            
            return newNode
        
        oldMap = {}
            
        return clone(node, oldMap)





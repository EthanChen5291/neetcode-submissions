class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodes = {i: [] for i in range(n)}

        for a, b in edges:
            nodes[a].append(b)
            nodes[b].append(a)

        visited = set()

        # in example, there are two ways to reach one node. so maintain visited, if you reach visited node from two different nodes

        def dfs(root: int, parent: int) -> bool:
            if root in visited:
                return False
            
            visited.add(root)

            for neighbor in nodes[root]: # graph root -> undirected edges. maintain visiting so that you know not to go back to prev
                if neighbor == parent:
                    continue
                
                if not dfs(neighbor, root):
                    return False

            return True
        
        if not dfs(0, -1):
            return False
        
        return len(visited) == n
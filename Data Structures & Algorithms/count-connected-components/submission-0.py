class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = {i: [] for i in range(n)}

        for a, b in edges:
            nodes[a].append(b)
            nodes[b].append(a)

        connected = 0

        visited = set()

        def dfs(node: int) -> bool: # True means new node, False means familiar
            if node in visited:
                return
            
            visited.add(node)

            for neighbor in nodes[node]:
                dfs(neighbor)
                
            return
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                connected += 1
            
        
        return connected








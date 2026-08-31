class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # dfs with a visited and visiting set

        # visiting 

        # if node in visiting:
        # parent -> node, maybe keep parent

        
        graph = {i: [] for i in range(1, len(edges) +1)}

        visited = set()

        def dfs(node: int, target: int, visited: dict) -> bool:
            if node == target:
                return True
            
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor, target, visited):
                        return True
            
            return False
        
        for a, b in edges:
            if dfs(a, b, set()):
                return [a, b]
        
            graph[a].append(b)
            graph[b].append(a)

        

            







class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        visiting = set()
        visited = set()

        def dfs(course: int) -> bool:
            if course in visiting:
                return False
            
            if course in visited:
                return True
            
            if not graph[course]:
                return True # or increment?
            
            visiting.add(course)

            for nextCourse in graph[course]:
                if not dfs(nextCourse):
                    return False
            
            visiting.remove(course)
            visited.add(course)

            return True
        
        for course, prereq in prerequisites:
            if not dfs(course):
                return False
        
        return True

        

        

            
            





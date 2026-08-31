class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        visiting = set()
        visited = set()

        def dfs(course) -> bool:
            if course in visiting:
                return False

            if course in visited:
                return True
            
            visiting.add(course)

            for nextCourse in graph[course]:
                if not dfs(nextCourse):
                    return False
            
            visited.add(course)
            visiting.remove(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
            
        return True

            
            





class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        indegreeMap = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegreeMap[course] += 1

        queue = deque()

        for course in range(numCourses):
            if indegreeMap[course] == 0:
                queue.append(course)
        
        complete = 0

        while queue:
            course = queue.popleft()

            complete += 1

            for nextCourse in graph[course]:
                indegreeMap[nextCourse] -= 1
                
                if indegreeMap[nextCourse] == 0:
                    queue.append(nextCourse)
        
        return complete == numCourses
            

            





        






        





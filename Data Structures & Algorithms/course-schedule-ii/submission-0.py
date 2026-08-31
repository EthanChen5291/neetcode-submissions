class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # use dfs, start from 0 and iterate until you reach numCourses-1

        # use bfs, start from 0 and reach every neighbor

        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        completed = 0
        res = []

        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        visited = []

        while queue:
            course = queue.popleft()

            completed += 1
            visited.append(course)

            for nextCourse in graph[course]:
                indegree[nextCourse] -= 1

                if indegree[nextCourse] == 0:
                    queue.append(nextCourse)

        if completed == numCourses:
            return visited
        else:
            return []




        
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {course:[] for course in range(numCourses)}

        indegree = [0]*numCourses

        for course,pre in prerequisites:
            graph[pre].append(course)
            indegree[course]+=1


        queue=deque()


        for course in range(numCourses):
            if indegree[course]==0:
                queue.append(course)
        
        result = []

        while queue:
            course = queue.popleft()

            result.append(course)

            for next_course in graph[course]:
                indegree[next_course] -=1

                if indegree[next_course]==0:
                    queue.append(next_course)
        
        if len(result) == numCourses:
            return result
        
        return []
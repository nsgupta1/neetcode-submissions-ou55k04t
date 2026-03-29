class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses  # [0,0,0 ....numCourses]
        adjMap = [[] for i in range(numCourses)]
        queue = deque()
        res = []
        for course, preq in prerequisites:
            indegree[preq] += 1
            adjMap[course].append(preq)
        
        # Initialize queue with courses of 0 dependency i.e. indegree 0
        for course, dep in enumerate(indegree):
            if dep == 0:
                queue.append(course)

        while queue:
            currCourse = queue.popleft()
            res.append(currCourse)
            
            for dep in adjMap[currCourse]:
                indegree[dep] -= 1
                if indegree[dep] == 0:
                    queue.append(dep)
        
        if len(res) != numCourses:
            return [] # cycle detected and some of the courses could not be completed

        return res[::-1]

        
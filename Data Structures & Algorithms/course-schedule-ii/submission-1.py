class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        visiting = set()
        courses = []
        adjMap = defaultdict(list)

        for course, preq in prerequisites:
            adjMap[course].append(preq)
        
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            visiting.add(course)
            for preq in adjMap[course]:
                if not dfs(preq):
                    return False
            visiting.remove(course)
            visited.add(course)
            courses.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
                
        return courses
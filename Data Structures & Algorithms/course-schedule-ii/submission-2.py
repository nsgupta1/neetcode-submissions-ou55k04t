class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        visiting = set()
        res = []

        adjMap = [[] for i in range(numCourses)] # 0 => [], 1 => [], 2 => []

        for course, preq in prerequisites:
            adjMap[course].append(preq)     # 0 => [], 1 => 0, 2 => []

        def dfs(course):
            if course in visiting:   # detect cycle
                return False
            if course in visited:
                return True
            visiting.add(course)
            for preq in adjMap[course]:
                if not dfs(preq):
                    return False
            visited.add(course)
            res.append(course)
            visiting.remove(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res

        
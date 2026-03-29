class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        visiting = set()
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
                print(preq)
                if not dfs(preq):
                    return False
            visiting.remove(course)
            visited.add(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
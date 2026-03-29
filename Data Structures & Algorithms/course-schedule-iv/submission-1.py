class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        '''
            1 - Create adjacency map for each prerequisites
            2 - Run DFS on each course and whatever is the dependency set merge it within the node
            3 - Once this set is ready after covering all courses, run queries and store res 
        '''

        adjMap = defaultdict(list)
        res = []
        indirectDepMap = defaultdict(set)
        visited = set()
        
        # create adjacency list for each course
        for preq, course in prerequisites:
            adjMap[course].append(preq)
        # [[1,0],[2,1],[3,2]]: 0->1, 1->2, 2->3, 3 -> []

        def dfs(course):
            if course in visited:
                return
            visited.add(course)
            for preq in adjMap.get(course, []):
                dfs(preq)
                indirectDepMap[course].update(indirectDepMap.get(preq, ())) # merge nested prerequisites
            indirectDepMap[course].update(adjMap.get(course, ())) # merge direct prerequisites

            
        for i in range(numCourses):
            dfs(i)

        for preq, course in queries:
            if preq in indirectDepMap.get(course, ()):
                res.append(True)
            else:
                res.append(False)
        return res
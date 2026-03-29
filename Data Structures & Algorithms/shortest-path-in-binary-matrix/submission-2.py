class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        src = (0, 0)
        dest = (len(grid), len(grid[0]))
        Applying BFS algorithm because bfs processes each node layer by layer and 
        guarantees that layer k will be reached before layer k+1, TC: O(m*n)
        DFS is more of a brute force solution with TC 4^m*n because dfs will process
        each path to reach destination and then find minimum
        """
        rows = len(grid)-1
        cols = len(grid[0])-1
        if grid[0][0] == 1 or grid[rows][cols] == 1:
            return -1
        visited = set()
        src = (0, 0, 1)
        queue = deque()
        queue.append(src)
        visited.add(src)

        dirs = [[1,0], [-1,0], [0,1], [0,-1], [-1,-1], [1, 1], [1, -1], [-1, 1]]

        while queue:
            r, c, length = queue.popleft()
            if r == rows and c == cols:
                return length
            
            for dr, dc in dirs:
                nr = r+dr
                nc = c+dc
                if (min(nr, nc) < 0 or nr > rows or nc > cols or 
                grid[nr][nc] == 1 or (nr, nc) in visited):
                    continue
                queue.append((nr, nc, length+1))
                visited.add((nr, nc))
        
        return -1
        
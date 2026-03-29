class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        1. BFS is the best algo for shortest path in unwieghted graphs
        2. Instead of BFS from rooms, start BFS from gates
        3. BFS from multiple gates at the same time will ensure we are 
            already putting shortest distance
        4. Mark visited locations in set
        5. SC: O(m*n) TC: O(m*n)
        """

        visited = set()
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        dirs = [[1,0], [0,1], [-1,0], [0,-1]]

        # Put all gates in queue first
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c,0))
                    visited.add((r,c))
        
        while queue:
            # process each level one by one, starting from all gates
            length = len(queue)
            for i in range(length):
                r, c, level = queue.popleft()
                for dr, dc in dirs:
                    nr = r+dr
                    nc = c+dc
                    if(min(nr, nc) < 0 or nr >= rows or nc >= cols or 
                    (nr, nc) in visited or grid[nr][nc] == -1):
                        continue
                    queue.append((nr, nc, level+1))
                    grid[nr][nc] = level+1
                    visited.add((nr,nc))
        
        
        
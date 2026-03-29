class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        1. Start from rotten fruits and mark new rotten fruits level by level(minute)
        2. Once all fruits have been marked rotten, return minimum amount of iterations
            it took to mark them rotten
        3. We can simultaneously run BFS from all rotten fruits in the grid
        4. Once queue is empty visit every node again to make sure there isn't any 
            fresh fruit remaining if there is any, return -1 else minutes for rotting
        5. OR keep count of fresh fruits and reduce that count while marking that fruit
            rotten, if 0 fresh fruits return minutes for rotting else -1
        """
        queue = deque()
        freshFruits = 0
        rows = len(grid)
        cols = len(grid[0])
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        minute = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    freshFruits += 1
                if grid[r][c] == 2:
                    queue.append((r,c))
        
        while queue and freshFruits > 0:
            length = len(queue)
            for i in range(length):
                r, c = queue.popleft()
                for dr, dc in dirs:
                    nr = r+dr
                    nc = c+dc
                    if(min(nr,nc) < 0 or nr >= rows or nc >= cols 
                    or grid[nr][nc] != 1):
                        continue
                    queue.append((nr, nc))
                    grid[nr][nc] = 2
                    freshFruits -= 1
            minute += 1

        return -1 if freshFruits > 0 else minute



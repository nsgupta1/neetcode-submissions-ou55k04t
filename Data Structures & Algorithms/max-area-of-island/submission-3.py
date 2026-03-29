class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        """
            1. Find an island and run a DFS on it to calculate it's area
            2. While running DFS make the island '0' or keep a set of seen indexes
            3. Maintain a global max and update it if a bigger area is found
            4. return the maxArea after grid is traversed fully
            5. TC: O(m*n) where m and n are rows and cols, size of the grid
            6. SC: if we keep seen set, O(m*n) else O(areaOfLargestIsland) for dfs recursive stack
        """
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j) -> int:
            if i < 0 or i == rows or j < 0 or j == cols or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            area = 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)  
            return area  

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    maxArea = max(maxArea, area)
        
        return maxArea

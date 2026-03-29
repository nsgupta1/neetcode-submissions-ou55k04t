class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int rowLen = grid.length;
        int colLen = grid[0].length;
        int maxArea = 0;
        for(int r = 0; r < rowLen; r++) {
            for(int c = 0; c < colLen; c++) {
                if(grid[r][c] == 1) {
                    int islandArea = calculateAreaOfIsland(grid, r, c, 0, rowLen, colLen);
                    maxArea = Math.max(maxArea, islandArea);
                }
            }
        }
        return maxArea;
    }

    private int calculateAreaOfIsland(int[][] grid, int r, int c, int area, int rowLen, int colLen) {
        if(r < 0 || r >= rowLen || c < 0 || c >= colLen || grid[r][c] == 0) return area;
        grid[r][c] = 0;
        area = calculateAreaOfIsland(grid, r-1, c, area, rowLen, colLen);
        area = calculateAreaOfIsland(grid, r+1, c, area, rowLen, colLen);
        area = calculateAreaOfIsland(grid, r, c+1, area, rowLen, colLen);
        area = calculateAreaOfIsland(grid, r, c-1, area, rowLen, colLen);
        return area+1;
    }
}

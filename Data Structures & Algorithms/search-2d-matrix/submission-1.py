class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        top, bottom = 0, rows-1
        # first binary search to find row which is m1
        while top <= bottom:
            row = top+(bottom-top)//2
            if target > matrix[row][-1]:
                top = row+1
            elif target < matrix[row][0]:
                bottom = row-1
            else:
                break

        l, r = 0, cols-1
        while l <= r:
            m2 = l+(r-l)//2
            if target > matrix[row][m2]:
                l = m2 + 1
            elif target < matrix[row][m2]:
                r = m2 - 1
            else:
                return True
        return False
                    
        

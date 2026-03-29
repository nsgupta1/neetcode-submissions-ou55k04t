class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        maxLeft = [0] * length
        maxRight = [0] * length
        area = 0
        for i in range(1, length):
            j = length-i-1
            maxLeft[i] = max(maxLeft[i-1], height[i-1])
            maxRight[j] = max(maxRight[j+1], height[j+1])
        
        for i in range(length):
            currArea = min(maxLeft[i], maxRight[i])-height[i]
            if currArea > 0:
                area += currArea
        return area 
        
    


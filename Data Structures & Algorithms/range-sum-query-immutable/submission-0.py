class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0] * len(nums)
        for i, num in enumerate(nums):
            self.prefix[i] = num + self.prefix[i-1] # for prefix[0] = prefix[-1]+num = 0+(-2) [-2,0,3,-5,2,-1]

    def sumRange(self, left: int, right: int) -> int:
        preRight = self.prefix[right]
        preLeft = self.prefix[left-1] if left > 0 else 0
        return preRight-preLeft
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
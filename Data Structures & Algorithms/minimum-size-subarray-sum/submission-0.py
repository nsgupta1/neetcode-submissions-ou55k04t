class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        sum = 0
        minWindow = float('inf') # or len(nums)+1
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target :
                minWindow = min(r-l+1, minWindow)
                sum -= nums[l]
                l += 1
        return 0 if minWindow == float('inf') else minWindow


        
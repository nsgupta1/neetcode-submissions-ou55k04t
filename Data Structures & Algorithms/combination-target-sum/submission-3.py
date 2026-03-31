class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        stack = []
        nums.sort()
        def backtrack(idx, currSum):
            if currSum == target:
                res.append(stack.copy())
                return
            if currSum > target or idx >= len(nums):
                return
            stack.append(nums[idx])
            backtrack(idx, currSum+nums[idx])
            stack.pop()
            backtrack(idx+1, currSum)
        
        backtrack(0, 0)
        return res
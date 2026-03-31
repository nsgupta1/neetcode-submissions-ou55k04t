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
            
            for i in range(idx, len(nums)):
                if currSum + nums[i] > target:
                    return
                stack.append(nums[i])
                backtrack(i, currSum+nums[i])
                stack.pop()
        
        backtrack(0, 0)
        return res
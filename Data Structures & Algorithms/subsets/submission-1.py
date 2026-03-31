class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        stack = []
        res = []

        def backtrack(idx):
            if idx >= len(nums):
                res.append(stack.copy())
                return
            stack.append(nums[idx])
            backtrack(idx+1)
            stack.pop()
            backtrack(idx+1)
        
        backtrack(0)
        return res
        
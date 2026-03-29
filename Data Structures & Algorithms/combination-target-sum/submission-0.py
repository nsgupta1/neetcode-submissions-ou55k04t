class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def backtrack(idx, currSum):
            if  idx >= len(nums) or currSum > target:
                return
            
            if currSum == target:
                res.append(curr.copy())
                return
            
            curr.append(nums[idx])
            backtrack(idx, currSum+nums[idx])
            
            curr.pop()
            backtrack(idx+1, currSum)

        backtrack(0, 0)
        return res
            

        
        
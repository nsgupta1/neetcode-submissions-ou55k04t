class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        nums.sort()

        def dfs(i, currSum):
            if currSum == target:
                res.append(curr.copy())
            
            for j in range(i, len(nums)):
                if currSum + nums[j] > target:
                    return
                curr.append(nums[j])   
                dfs(j, currSum+nums[j])
                curr.pop()
        dfs(0, 0)    
        return res
                
        
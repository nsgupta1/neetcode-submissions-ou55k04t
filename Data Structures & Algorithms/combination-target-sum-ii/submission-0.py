class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        nums.sort()

        def dfs(i, currSum):
            if currSum == target:
                res.append(curr.copy())
                return

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                if nums[j] + currSum > target:
                    return
                curr.append(nums[j])
                dfs(j+1, currSum+nums[j])
                curr.pop() 
        dfs(0,0)
        return res
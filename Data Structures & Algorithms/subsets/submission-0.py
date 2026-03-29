class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(idx, subset) :
            if idx >= len(nums):
                res.append(subset.copy())
                return
            num = nums[idx]
            subset.append(num)
            idx = idx+1
            backtrack(idx, subset)
            subset.pop()
            backtrack(idx, subset)

        backtrack(0, [])
        
        return res

            
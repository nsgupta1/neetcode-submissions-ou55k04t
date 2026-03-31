class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        stack = []
        res = []
        candidates.sort()

        def backtrack(idx, currSum):
            if currSum == target:
                res.append(stack.copy())
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue 
                if currSum + candidates[i] > target:
                    return
                stack.append(candidates[i])
                backtrack(i+1, currSum + candidates[i])
                stack.pop()
        
        backtrack(0,0)
        return res
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        candidates.sort()

        def backtrack(i, currSum):
            if currSum == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or currSum+candidates[i] > target:
                return
            curr.append(candidates[i])
            backtrack(i+1, currSum+candidates[i])
            curr.pop()
            
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, currSum)
        
        backtrack(0, 0)
        return res
            

             
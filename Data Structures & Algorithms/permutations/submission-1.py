class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        unique = set()
        res = []
        stack = []

        def backtrack():
            if len(stack) == len(nums):
                res.append(stack.copy())
                return
            
            for num in nums:
                if num in unique:
                    continue
                stack.append(num)
                unique.add(num)
                backtrack()
                stack.pop()
                unique.remove(num)
            
        backtrack()
        return res


        
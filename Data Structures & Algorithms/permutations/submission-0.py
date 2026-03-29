class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        perm = []
        isVisited = set()

        def backtrack():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for i in range(len(nums)):
                if nums[i] not in isVisited:
                    perm.append(nums[i])
                    isVisited.add(nums[i])
                    backtrack()
                    perm.pop()
                    isVisited.discard(nums[i])

        backtrack()
        return res


        
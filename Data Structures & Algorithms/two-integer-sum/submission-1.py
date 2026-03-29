class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i in range(len(nums)):
            curr = target-nums[i]
            if curr in store:
                return [store[curr], i]
            store[nums[i]] = i
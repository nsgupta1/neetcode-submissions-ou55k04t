class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        store = set()
        L = 0
        if k == 0: return False
        for R in range(len(nums)): 
            if nums[R] in store:
                return True
            store.add(nums[R])
            if len(store) > k:
                store.remove(nums[L])
                L += 1
        return False
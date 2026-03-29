class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Array not rotated
        if nums[0] <= nums[-1]:
            return self.binarySearch(nums,0, len(nums)-1, target)

        # Find the pivot point
        l, r = 0, len(nums)-1
        pivot = 0
        while l <= r:
            mid = l+(r-l)//2
            if nums[mid] < nums[mid-1]:
                pivot = mid
                break
            elif nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid - 1

        # check in which half we need to apply binary search 
        if nums[0] <= target <= nums[pivot-1]:
            return self.binarySearch(nums, 0, pivot-1, target)
        return self.binarySearch(nums, pivot, len(nums)-1, target)

    
    def binarySearch(self, nums:List[int],l, r, target: int) -> int:
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1
        
        
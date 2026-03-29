class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            target = 0 - nums[i]
            l = i+1
            r = len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                sum = nums[l] + nums[r]
                if sum > target:
                    r -= 1
                elif sum < target:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l, r = l+1, r-1
                    while l < r and nums[l] == nums[l-1]:
                        l +=1
        return res


        
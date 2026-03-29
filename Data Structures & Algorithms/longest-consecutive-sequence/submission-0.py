class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        longestSet = set()
        for num in nums:
            if num in longestSet:
                continue
            curr = num
            temp = set()
            while curr in store:
                temp.add(curr)
                curr += 1
            if len(temp) > len(longestSet):
                longestSet = temp
        return len(longestSet)


            

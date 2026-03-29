class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        longestSeq = 0
        for num in nums:
            if num-1 in store:
                continue
            curr = num
            while curr in store:
                curr += 1
            length = curr-num
            longestSeq = max(longestSeq, length)
        return longestSeq


            

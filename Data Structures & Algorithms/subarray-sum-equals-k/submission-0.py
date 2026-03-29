class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
            Notes : Non intuitive approach
            1. Prefix sum concept, Range Sum Query Immutable where currSum = prefixLeft - preFixRight
            2. 
        '''
        currSum = 0
        prefMap = defaultdict(int)
        prefMap[0] += 1
        res = 0
        
        for n in nums:
            currSum += n
            diff = currSum - k
            res += prefMap.get(diff, 0)
            prefMap[currSum] += 1
        return res

        
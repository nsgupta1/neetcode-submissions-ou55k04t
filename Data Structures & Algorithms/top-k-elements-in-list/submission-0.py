class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        # Count frequency of each element
        for n in nums:
            count[n] += 1
        
        # For Bucket sort technique find the maximum frequency
        maxFreq = -1
        for val in count.values():
            if val > maxFreq:
                maxFreq = val
        
        # Create array of buckets from 1 to maxFreq
        buckets = [[] for i in range(maxFreq+1)]
        for num, cnt in count.items():
            buckets[cnt].append(num)

        res = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
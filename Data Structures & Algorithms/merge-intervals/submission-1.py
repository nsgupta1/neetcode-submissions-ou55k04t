class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        res = []
        # Sort intervals by start time and if start time is equal then use end time
        interval_sorted = sorted(intervals, key=lambda x:(x[0],x[1]))
        curr = interval_sorted[0]
        for i in range(1, len(interval_sorted)):
            next = interval_sorted[i]
            if curr[1] >= next[0]:
                curr = [curr[0], max(curr[1], next[1])]
            else:
                res.append(curr)
                curr = next
        res.append(curr)
        return res
        
        '''
        curr = [1,3] 
        next = [1,5] 
        if overlap(curr, next):
            interval = merge(curr, next)
        else:
            res.append(curr)
            curr = next
        res.append(curr)
        return res
        '''
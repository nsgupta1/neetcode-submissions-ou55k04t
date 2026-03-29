class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Perform Binary search on 1 to max 
        l = 1
        r = max(piles) # O(n)
        prevSpeed = 0

        while l <= r:   # (log(m)) m is the max value
            mid = l + (r-l)//2
            total = 0
            for p in piles: # O(log(n))
                total += math.ceil(float(p) / mid)
            if total <= h:
                r = mid-1
                prevSpeed = mid
            else:
                l = mid+1
        return prevSpeed


        
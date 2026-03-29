class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0 # it just denotes starting point
        sum = 0
        subarray = 0
        for r in range(len(arr)):
            sum += arr[r]
            if r-l+1 == k:
                avg = sum/k
                if avg >= threshold:
                    subarray += 1
                sum -= arr[l]
                l += 1
        return subarray

        
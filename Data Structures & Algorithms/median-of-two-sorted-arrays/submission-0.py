class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr1, arr2 = nums1, nums2
        len1, len2 = len(nums1), len(nums2)
        total = len1 + len2
        half = total // 2
    
        if len2 < len1:
           arr1, arr2 = nums2, nums1
           len1, len2 = len2, len1

        l, r = 0, len1 - 1
    
        while True:
            m1 = (l + r) //2 
            m2 = half - (m1 + 1) - 1

            # Left Partition is Arr1 - 0 to m1 and Arr2 0 to m2
            aleft = arr1[m1] if m1 >= 0 else float('-inf')
            aright = arr1[m1 + 1] if m1 + 1 < len1 else float('inf')
            bleft = arr2[m2] if m2 >= 0 else float('-inf')
            bright = arr2[m2 + 1] if m2 + 1 < len2 else float('inf')

            if aleft <= bright and bleft <= aright:
                if total % 2:
                    return min(aright, bright)
                return (max(aleft, bleft) + min(aright, bright)) / 2
            
            if aleft > bright:
                r = m1 - 1
            else:
                l = m1 + 1
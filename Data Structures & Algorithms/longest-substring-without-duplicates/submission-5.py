class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        unique = set()
        maxLen = 0
        for r in range(len(s)):
            if s[r] in unique:
                maxLen = max(maxLen, r-l)
                while s[r] != s[l]:
                    unique.discard(s[l])
                    l += 1
                l += 1
            else:
                unique.add(s[r])
                maxLen = max(maxLen, r-l+1)
        return maxLen

            

        
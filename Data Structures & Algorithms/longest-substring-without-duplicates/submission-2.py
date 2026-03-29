class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        maxLen = 0
        store = set()
        for i in range(len(s)):
            while s[i] in store:
                store.remove(s[start])
                start += 1
            store.add(s[i])
            maxLen = max(i-start + 1, maxLen)
        return maxLen

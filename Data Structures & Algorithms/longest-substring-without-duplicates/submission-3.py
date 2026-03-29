class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        maxLen = 0
        store = set()
        for i in range(len(s)):
            duplicate = s[i]
            while duplicate in store:
                store.remove(s[start])
                start += 1
            store.add(duplicate)
            maxLen = max(i-start + 1, maxLen)
        return maxLen

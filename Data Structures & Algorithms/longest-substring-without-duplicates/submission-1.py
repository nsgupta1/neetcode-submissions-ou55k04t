class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        maxLen = 0
        store = {}
        for i in range(len(s)):
            if s[i] in store:
                duplicate = store[s[i]]
                for j in range(start, duplicate+1):
                    store.pop(s[j])
                start = duplicate+1
            store[s[i]] = i
            maxLen = max(i-start + 1, maxLen)
        return maxLen

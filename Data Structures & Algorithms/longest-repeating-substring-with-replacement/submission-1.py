class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = defaultdict(int)
        left = 0
        maxLen = 0
        for rt in range(len(s)):
            freqMap[s[rt]] += 1
            while (rt-left+1-max(freqMap.values())) > k:
                freqMap[s[left]] -= 1
                left += 1
            maxLen = max(rt-left+1, maxLen)
        return maxLen
        
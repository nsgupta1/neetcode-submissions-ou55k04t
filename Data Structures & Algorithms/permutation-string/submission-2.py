class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Freq = {}
        currFreq = {}
        match = 0
        left = 0

        for s in s1:
           s1Freq[s] = s1Freq.get(s, 0)+1
        
        for r in range(len(s2)):
            c = s2[r]
            if c in s1Freq:
                currFreq[c] = currFreq.get(c, 0) + 1
                match += 1
                while currFreq[c] > s1Freq[c]:
                    currFreq[s2[left]] -= 1
                    left += 1
                    match -= 1
            else:
                currFreq = {}
                match = 0
                left = r + 1
            if (match == len(s1)):
                return True
        return False

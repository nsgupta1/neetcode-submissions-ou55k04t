class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Freq = {}
        currFreq = {}
        left, match = 0, 0

        for c in s1:
            s1Freq[c] = s1Freq.get(c, 0)+1
        
        for r in range(len(s2)):
            c = s2[r]
            if c in s1Freq:
                currFreq[c] = currFreq.get(c, 0)+1
                match += 1
                # Abandon old matches until freq are equal
                while currFreq[c] > s1Freq[c]:
                    currFreq[s2[left]] -= 1
                    left += 1
                    match -= 1
        # if distinct char came in between matches, abandon entire hm and start fresh
            else:
                currFreq = {}
                match = 0
                left = r + 1
            if (match == len(s1)):
                return True
        return False

            
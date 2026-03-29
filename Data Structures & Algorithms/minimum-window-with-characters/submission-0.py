class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return t
        tFreq = {}
        currFreq = {}
        have = 0
        left = 0
        res = [-1, -1]
        maxRes = float('inf')
        
        for c in t:
            tFreq[c] = tFreq.get(c, 0)+1
        
        need = len(tFreq)

        for r in range(len(s)):
            c = s[r]
            currFreq[c] = currFreq.get(c, 0)+1
            if c in tFreq and currFreq[c] == tFreq[c]:
                have += 1
            while have == need:
                l = s[left]
                if r-left+1 < maxRes:
                    maxRes = r-left+1
                    res = [left,r]
                currFreq[l] -= 1
                left += 1
                if l in tFreq and currFreq[l] < tFreq[l]:
                    have -= 1
        
        return s[res[0]:res[1]+1] if maxRes < float('inf') else ""

                

        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = re.sub(r'[\W]+','',s.lower())
        for i in range(len(clean)):
            j = len(clean)-1-i
            if clean[i] != clean[j]:
                return False
        return True
class Solution:
    """
        1. backtrack with base condition, countOpen = countClosed = n, append array to string
        2. Start with open always and close only if countClosed < countOpen
    """
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def backtrack(countOpen, countClose):
            if countOpen == n and countClose == n:
                res.append("".join(curr.copy()))
                return
            if countOpen < n:
                curr.append("(")
                backtrack(countOpen+1, countClose)
                curr.pop()
            if countClose < countOpen:
                curr.append(")")
                backtrack(countOpen, countClose+1)
                curr.pop()
        backtrack(0,0)
        return res
            


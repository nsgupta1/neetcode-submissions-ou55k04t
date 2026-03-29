class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        amSet = {'+', '-', '*', '/'} # set can also be declared like this

        for c in tokens:
            if c in amSet:
                r = stack.pop()
                l = stack.pop()
                val = 0
                if c == '+': val = l + r
                elif c == '-': val = l-r
                elif c == '*': val = l*r
                else: val = int(l/r)
                stack.append(val)
            else:
                stack.append(int(c))
        return stack[0] if stack else 0

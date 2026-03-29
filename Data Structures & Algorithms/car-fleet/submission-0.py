class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        stack = []
        for p in pair:
            dist = (target-p[0])/p[1]
            if not stack or dist > stack[-1]:
                stack.append(dist)
        return len(stack)
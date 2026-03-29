class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        maxStack = []
        res = [0]*len(temp)
        for i in range(len(temp)):
            while maxStack and temp[i] > maxStack[-1][0]:
                t, idx = maxStack.pop()
                res[idx] = i - idx
            maxStack.append([temp[i], i])
        return res
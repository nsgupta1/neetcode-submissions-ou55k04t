class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            maxProfit = max(prices[i] - minBuy, maxProfit)
            minBuy = min(prices[i], minBuy)
        
        return maxProfit

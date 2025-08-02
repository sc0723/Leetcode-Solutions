class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalProfit = 0
        lastPrice = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                totalProfit += (prices[i] - lastPrice)
            lastPrice = prices[i]

        return totalProfit
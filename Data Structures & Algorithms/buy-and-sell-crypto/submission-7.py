class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0
        for r in range(1, len(prices)):
            profit = max(profit, prices[r] - prices[l])
            if prices[l] > prices[r]:
                l = r
        return profit

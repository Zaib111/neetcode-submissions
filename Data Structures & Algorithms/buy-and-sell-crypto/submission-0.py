class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_difference = 0
        # Brute force solution
        for i in range(len(prices)):
            for j in range(len(prices)):
                if j > i:
                    max_difference = max(max_difference, prices[j] - prices[i])
        return max_difference

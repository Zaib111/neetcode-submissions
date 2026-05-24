class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_difference = 0
        # # Brute force solution
        # for i in range(len(prices)):
        #     for j in range(len(prices)):
        #         if j > i:
        #             max_difference = max(max_difference, prices[j] - prices[i])
        # return max_difference

        buy, sell = 0, 1
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                max_difference = max(max_difference, prices[sell] - prices[buy])
            else: # this means we have negative profit, which we don't want regardless
                # we want to buy as low as possible, and sell as high as possible, so make buy the higher one
                buy = sell
            sell += 1

        return max_difference
        # [7, 2, 1, 10, 5]


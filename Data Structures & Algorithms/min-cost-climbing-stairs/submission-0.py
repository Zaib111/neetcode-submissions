class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = cost[-1], 0
        for i in range(len(cost) - 2, -1, -1):
            temp = one
            one = cost[i] + min(one, two)
            two = temp
        return min(one, two)
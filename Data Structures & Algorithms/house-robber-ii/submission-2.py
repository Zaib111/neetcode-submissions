class Solution:
    def rob(self, nums: List[int]) -> int:
        firstRob1, secondRob1, firstRob2, secondRob2 = 0, 0, 0, 0
        for i in range(len(nums) - 1):
            temp1 = secondRob1
            secondRob1 = max(firstRob1 + nums[i], secondRob1)
            firstRob1 = temp1

            temp2 = secondRob2
            secondRob2 = max(firstRob2 + nums[i + 1], secondRob2)
            firstRob2 = temp2
        if len(nums) == 1: return nums[0]
        return max(secondRob1, secondRob2)
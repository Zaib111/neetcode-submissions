class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.helper(nums, 0, len(nums) - 1), self.helper(nums, 1, len(nums)), nums[0])
    
    def helper(self, nums, start, end):
        one, two = 0, 0
        for i in range(start, end):
            temp = two
            two = max(one + nums[i], two)
            one = temp
        return two
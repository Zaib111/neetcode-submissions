class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0
        for num in nums:
            temp = two
            two = max(two, one + num)
            one = temp
        return two
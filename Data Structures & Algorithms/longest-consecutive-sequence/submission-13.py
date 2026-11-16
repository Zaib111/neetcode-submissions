class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums:
                cur_len = 1
                cur = num
                while cur + 1 in nums:
                    cur_len += 1
                    cur += 1
                res = max(res, cur_len)
        return res

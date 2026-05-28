class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0
        for num in nums:
            if num - 1 not in num_set:
                counter = 1
                while num + counter in num_set:
                    counter += 1
                max_len = max(max_len, counter)
        return max_len

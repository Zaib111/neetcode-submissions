class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_sequence = 0

        for num in nums:
            if num - 1 not in nums_set: # checking if this is a valid sequence
                length = 0 # length of sequence
                while num + length in nums_set:
                    length += 1
                longest_sequence = max(longest_sequence,length)
        return longest_sequence
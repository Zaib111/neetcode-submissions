class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = [[] for _ in range(len(nums) + 1)]
        # iterate backwards through freq to get top k elems
        num_to_freq = {}
        for num in nums:
            num_to_freq[num] = num_to_freq.get(num, 0) + 1
        for num in num_to_freq:
            freq[num_to_freq[num]].append(num)
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                k -= 1
                if k == 0:
                    return res
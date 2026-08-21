class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        num_to_freq = defaultdict(int)
        res = []
        for num in nums:
            num_to_freq[num] += 1
        for num in num_to_freq:
            freq[num_to_freq[num]].append(num)
        for i in range(len(nums), -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
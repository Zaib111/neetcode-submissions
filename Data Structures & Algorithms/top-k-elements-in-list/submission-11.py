class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        for num in count:
            bucket[count[num]].append(num)
        
        for i in range(len(nums), -1, -1):
            for num in bucket[i]:
                res.append(num)
                k -= 1
                if k == 0: return res
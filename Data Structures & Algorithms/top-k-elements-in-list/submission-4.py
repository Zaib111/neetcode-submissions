class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = {}
        max_so_far = -1
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for _ in range(k):
            for num in count:
                if count[num] == max(count.values()):
                    res.append(num)
                    max_so_far = num
                    break
            count.pop(max_so_far)
        return res
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # hashmap to count the occurrences of each value
        freq = [[] for i in range(len(nums) + 1)] # index will be count of that element and value will be the list of values that occur that many times

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for value, occurrence in count.items(): # every key-value pair in count dictionary
            freq[occurrence].append(value)

        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res

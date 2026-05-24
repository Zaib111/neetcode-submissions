class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = []
        for num in nums:
            if num not in res:
                res.append(num)
            else:
                return True
        return False
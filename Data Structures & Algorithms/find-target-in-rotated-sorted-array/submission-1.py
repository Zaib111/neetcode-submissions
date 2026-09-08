class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]: return m
            elif nums[m] >= nums[l]:
                if target < nums[l] or nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target >= nums[l] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        
        return -1
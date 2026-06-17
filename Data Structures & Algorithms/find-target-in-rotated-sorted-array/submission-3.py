class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[l] <= nums[r]:
                while l <= r:
                    m = (l + r) // 2
                    if target > nums[m]:
                        l = m + 1
                    elif target < nums[m]:
                        r = m - 1
                    else:
                        return m
                break
            if target > nums[m] and nums[m] >= nums[l]:
                l = m + 1
            elif target < nums[m] and nums[m] >= nums[l]:
                if target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            elif target > nums[m] and nums[m] < nums[l]:
                if target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            elif target < nums[m] and nums[m] < nums[l]:
                r = m - 1
            elif target == nums[m]:
                return m

        return -1
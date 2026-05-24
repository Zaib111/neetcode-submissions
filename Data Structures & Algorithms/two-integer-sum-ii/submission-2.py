class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r: # guaranteed that our loop will return a solution
            curr_sum = numbers[l] + numbers[r]
            if curr_sum < target:
                l += 1
            elif curr_sum > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        return [] # this will never happen, since we're guaranteed a solution
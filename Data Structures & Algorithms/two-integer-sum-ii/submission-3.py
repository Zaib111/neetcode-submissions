class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            sum_so_far = numbers[l] + numbers[r]
            if sum_so_far == target:
                return [l + 1, r + 1]
            if sum_so_far < target:
                l += 1
            else:
                r -= 1
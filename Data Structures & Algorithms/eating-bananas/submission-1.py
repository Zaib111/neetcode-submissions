class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        nums = []
        res = float("infinity")
        l, r = 0, max(piles) - 1
        while l <= r:
            m = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/(m + 1))
            if hours <= h:
                res = min(res, m + 1)
                r = m - 1
            else:
                l = m + 1
        return res
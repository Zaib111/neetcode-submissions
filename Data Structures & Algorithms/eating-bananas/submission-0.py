class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, max(piles) - 1
        res = float("infinity")

        while l <= r:
            m = (l + r) // 2
            counter = 0
            for pile in piles:
                counter += math.ceil(pile/(m + 1))
            if counter <= h:
                res = min(res, m + 1)
                r = m - 1
            else:
                l = m + 1
        return res
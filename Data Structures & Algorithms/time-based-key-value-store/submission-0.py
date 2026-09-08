class TimeMap:

    def __init__(self):
        self.map = defaultdict(list) # {key: [(value, timestamp)]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        lst = self.map[key]
        l, r = 0, len(lst) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if lst[m][1] <= timestamp:
                res = lst[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
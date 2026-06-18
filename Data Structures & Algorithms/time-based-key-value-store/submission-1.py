class TimeMap:

    def __init__(self):
        self.res = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.res[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.res[key]) - 1
        temp = ""
        while l <= r:
            mid = (l + r) // 2
            if self.res[key][mid][0] <= timestamp:
                l = mid + 1
                temp = self.res[key][mid][1]
            else:
                r = mid - 1
        return temp
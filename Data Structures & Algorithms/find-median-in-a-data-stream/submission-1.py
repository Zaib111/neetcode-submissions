class MedianFinder:

    def __init__(self):
        self.smallHeap = []
        self.bigHeap = []
        heapq.heapify(self.smallHeap)
        heapq.heapify(self.bigHeap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallHeap, -num)
        if self.smallHeap and self.bigHeap and -self.smallHeap[0] > self.bigHeap[0]:
            smallMax = -heapq.heappop(self.smallHeap)
            heapq.heappush(self.bigHeap, smallMax)
        if len(self.smallHeap) - len(self.bigHeap) > 1:
            smallMax = -heapq.heappop(self.smallHeap)
            heapq.heappush(self.bigHeap, smallMax)
        if len(self.bigHeap) - len(self.smallHeap) > 1:
            bigMin = -heapq.heappop(self.bigHeap)
            heapq.heappush(self.smallHeap, bigMin)

    def findMedian(self) -> float:
        if len(self.smallHeap) == len(self.bigHeap):
            return (-self.smallHeap[0] + self.bigHeap[0]) / 2
        if len(self.smallHeap) > len(self.bigHeap):
            return -self.smallHeap[0]
        return self.bigHeap[0]
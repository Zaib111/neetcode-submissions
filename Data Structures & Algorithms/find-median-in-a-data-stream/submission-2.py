class MedianFinder:

    def __init__(self):
        self.leftHeap = [] # max heap
        self.rightHeap = [] # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.leftHeap, -num)

        if self.leftHeap and self.rightHeap and -self.leftHeap[0] > self.rightHeap[0]:
            leftMax = -heapq.heappop(self.leftHeap)
            heapq.heappush(self.rightHeap, leftMax)
        if len(self.leftHeap) - len(self.rightHeap) > 1:
            leftMax = -heapq.heappop(self.leftHeap)
            heapq.heappush(self.rightHeap, leftMax)
        elif len(self.rightHeap) - len(self.leftHeap) > 1:
            rightMax = -heapq.heappop(self.rightHeap)
            heapq.heappush(self.leftHeap, rightMax)

    def findMedian(self) -> float:
        if len(self.leftHeap) > len(self.rightHeap):
            return -self.leftHeap[0]
        if len(self.leftHeap) < len(self.rightHeap):
            return self.rightHeap[0]
        return (-self.leftHeap[0] + self.rightHeap[0]) / 2
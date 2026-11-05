class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # maintain heap of size k and so the smallest will always be the kth largest.
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        while len(nums) > k:
            heapq.heappop(nums)


    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]
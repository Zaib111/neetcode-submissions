class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # maintain heap of size k and so the smallest will always be the kth largest.
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        while len(nums) > k:
            heapq.heappop(nums)


    def add(self, val: int) -> int:
        if len(self.min_heap) == self.k:
            if self.min_heap[0] < val:
                heapq.heappop(self.min_heap)
                heapq.heappush(self.min_heap, val)
        else:
            heapq.heappush(self.min_heap, val)

        return self.min_heap[0]
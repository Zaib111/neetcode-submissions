class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-1 * stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            y, x = -heapq.heappop(max_heap), -heapq.heappop(max_heap)
            if x < y:
                heapq.heappush(max_heap, -(y - x))
        return -max_heap[0] if max_heap else 0
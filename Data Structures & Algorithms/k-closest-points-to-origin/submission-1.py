class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        res = []
        heapq.heapify(max_heap)
        for x, y in points:
            dist = -math.sqrt(x**2 + y**2)
            heapq.heappush(max_heap, (dist, [x, y]))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        for pair in max_heap:
            res.append(pair[1])
        return res
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = stones[0]
            heapq.heappop(stones)
            y = stones[0]
            heapq.heappop(stones)
            if x < y:
                y = -(y - x)
                heapq.heappush(stones, y)
        return -stones[0] if stones else 0
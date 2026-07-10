class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-count for count in counts.values()]
        q = deque()
        time = 0
        heapq.heapify(max_heap)
        while max_heap or q:
            time += 1
            if max_heap:
                count = 1 + heapq.heappop(max_heap)
                if count:
                    q.append([count, time + n])
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time

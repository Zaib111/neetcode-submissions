class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1
        self.tweetMap[userId].append([self.count, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followMap[userId].add(userId)
        max_heap = []
        res = []
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                max_heap.append([count, tweetId, followeeId, index - 1])
        heapq.heapify(max_heap)
        while max_heap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(max_heap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(max_heap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
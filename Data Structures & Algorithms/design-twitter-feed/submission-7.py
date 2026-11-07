class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set) # followerId: {followeeId1, ..., }
        self.tweetMap = defaultdict(list) # userId: [[time, tweetId]]
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.tweetMap[userId].append([self.time, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            tweet_info = self.tweetMap[followeeId]
            if tweet_info:
                min_heap.append([tweet_info[-1][0], tweet_info[-1][1], len(tweet_info) - 1, followeeId])
        heapq.heapify(min_heap)
        res = []
        while len(res) < 10 and min_heap:
            time, tweetId, index, followeeId = heapq.heappop(min_heap)
            res.append(tweetId)
            if index >= 1:
                new_tweet_info = self.tweetMap[followeeId]
                heapq.heappush(min_heap, [new_tweet_info[index - 1][0], new_tweet_info[index - 1][1], index - 1, followeeId])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followMap[followerId]:
            return
        self.followMap[followerId].remove(followeeId)

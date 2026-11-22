class Twitter:

    def __init__(self):
        self.feed_map = defaultdict(list)
        self.follow_map = defaultdict(set)
        self.feed = []
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed_map[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = [userId]
        for following in self.follow_map[userId]:
            users.append(following)
        tweetIds = []
        heapq.heapify(tweetIds)
        for user in users:
            for post in self.feed_map[user]:
                heapq.heappush(tweetIds, post)
                if len(tweetIds) > 10:
                    heapq.heappop(tweetIds)
        res = []
        while tweetIds:
            post = heapq.heappop(tweetIds)
            res.append(post[1])
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follow_map[followerId]:
            self.follow_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
        
        

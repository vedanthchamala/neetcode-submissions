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
        users = set(self.follow_map[userId])
        users.add(userId)

        heap = []
        for user in users:
            tweets = self.feed_map[user]
            if tweets:
                idx = len(tweets) - 1
                time, tweetID = tweets[idx]
                heap.append((time, tweetID, user, idx))
        heapq.heapify_max(heap)
        res = []
        while heap and len(res) < 10:
            _, tweetID, user, idx = heapq.heappop_max(heap)
            res.append(tweetID)
            if idx > 0:
                time, nextId = self.feed_map[user][idx - 1]
                heapq.heappush_max(heap, (time, nextId, user, idx - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follow_map[followerId]:
            self.follow_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
        
        

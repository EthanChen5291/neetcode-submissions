class Twitter:

    def __init__(self):
        
        self.userMap = {} # user: [followees]
        self.newsFeed = {} # user: [(timestamp, tweetId)]
        self.tweets = {} # heap sorted from most to least recent (number timestamp)
        # tweets -> (timestamp, tweetId)
        self.feedSize = 10
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if not userId in self.tweets:
            self.tweets[userId] = []
        
        self.tweets[userId].append((-self.time, tweetId))
        self.time += 1

        return
        

    def getNewsFeed(self, userId: int) -> List[int]:
        
        ownPosts = self.tweets.get(userId, [])
        globalHeap = ownPosts.copy()

        heapq.heapify(globalHeap)

        followers = self.userMap.get(userId, [])
        res = []

        # make sure to catch if not enough posts case
        for f in followers:
            tweets = self.tweets.get(f, [])

            for t in tweets:
                heapq.heappush(globalHeap, t)

        while len(res) < 10 and globalHeap: # make sure to catch if not enough posts case
            if not globalHeap:
                break # just break for now

            latestTimestamp, latestTweet = heapq.heappop(globalHeap)
            
            res.append(latestTweet)
        
        return res

        



    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userMap:
            self.userMap[followerId] = []

        if followeeId not in self.userMap[followerId]:
            self.userMap[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.userMap and followeeId in self.userMap[followerId]:
            self.userMap[followerId].remove(followeeId)
        
        return

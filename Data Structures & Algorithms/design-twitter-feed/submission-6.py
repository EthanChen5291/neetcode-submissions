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
        globalHeap = []
        res = []

        users = self.userMap.get(userId, []).copy()
        users.append(userId)

        # make sure to catch if not enough posts case
        for u in users:
            tweets = self.tweets.get(u, [])

            if tweets:
                index = len(tweets) - 1

                time, tweetId = tweets[index]

                heapq.heappush(
                    globalHeap, 
                    (time, tweetId, u, index)
                    )
            
        while len(res) < 10 and globalHeap:
            time, tweetId, user, index = heapq.heappop(globalHeap)

            res.append(tweetId)

            index -= 1

            if index >= 0:
                nextTime, nextTweetId = self.tweets[user][index]
                heapq.heappush(
                    globalHeap, 
                    (nextTime, nextTweetId, user, index)
                    )
        
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

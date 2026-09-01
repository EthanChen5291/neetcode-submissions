class Twitter:

    def __init__(self):
        self.userMap = {} # user : followees
        self.tweetMap = {} # user : posts -> (timestamp, tweetID)
        self.newsFeedSize = 10
        self.timestamp = 0
        # min-heap -> each timestamp is negative 

        # global most recent tweet IDs


    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetMap:
            self.tweetMap[userId] = []

        self.tweetMap[userId].append((-self.timestamp, tweetId))
        self.timestamp += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        users = [userId]

        if userId in self.userMap:
            users += self.userMap[userId]

        for user in users:
            if user in self.tweetMap and self.tweetMap[user]:
                index = len(self.tweetMap[user]) - 1

                timestamp, tweetId = self.tweetMap[user][index]

                heapq.heappush(heap, (timestamp, tweetId, user, index)) # pop -> popleft (deque())
        
        res = []

        while heap and len(res) < self.newsFeedSize:
            if heap:
                timestamp, tweetId, author, index = heapq.heappop(heap)
                res.append(tweetId)

                if index > 0:
                    index -= 1

                    timestamp, tweetId = self.tweetMap[author][index]

                    heapq.heappush(heap, (timestamp, tweetId, author, index))
        
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.userMap: # consider changing to list
            self.userMap[followerId] = []
        
        if followeeId not in self.userMap[followerId]:
            self.userMap[followerId].append(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userMap:
            return 

        if followeeId not in self.userMap[followerId]:
            return 
        
        self.userMap[followerId].remove(followeeId)
        
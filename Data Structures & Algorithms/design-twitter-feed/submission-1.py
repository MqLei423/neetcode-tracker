class Twitter:

    def __init__(self):
        self.follows = defaultdict(set) #user->followeeId
        self.tweets = defaultdict(list) #user->(time,tweetId)
        self.time = 0 #decrement for maxHeap

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res,heap = [],[]
        self.follows[userId].add(userId)
        for followee in self.follows[userId]:
            if self.tweets[followee]:
                i = len(self.tweets[followee])-1
                time,tweet = self.tweets[followee][i]
                heapq.heappush(heap,(time,tweet,followee,i-1))
        while heap and len(res)<10:
            _,tweet,followee,i = heapq.heappop(heap)
            res.append(tweet)
            if i>=0:
                nxtTime,nxtTwt = self.tweets[followee][i]
                heapq.heappush(heap,(nxtTime,nxtTwt,followee,i-1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

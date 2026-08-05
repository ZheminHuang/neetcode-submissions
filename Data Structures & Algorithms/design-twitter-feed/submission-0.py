class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        max_heap = []

        users = self.following[userId]|{userId}

        for user in users:
            if self.tweets[user]:
                index = len(self.tweets[user])-1
                time,tweet_id = self.tweets[user][index]

                heapq.heappush(max_heap,(-time,tweet_id,user,index))
        
        while max_heap and len(result)<10:
            negative_time,tweet_id,user,index = heapq.heappop(max_heap)
            result.append(tweet_id)

            previous_index = index-1

            if previous_index>=0:
                time,previous_tweet_id = self.tweets[user][previous_index]
                heapq.heappush(max_heap,(-time,previous_tweet_id,user,previous_index))
        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


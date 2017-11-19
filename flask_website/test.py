from twitter.tweetcontainer import TweetContainer
tweetContainer = TweetContainer('realDonaldTrump')
tweetContainer.load(20)
print(tweetContainer.toDict(3))
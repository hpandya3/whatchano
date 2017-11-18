from twitter.tweetcontainer import TweetContainer
tweetContainer = TweetContainer('realDonaldTrump')
tweetContainer.load(5)
print(tweetContainer.__dict__)
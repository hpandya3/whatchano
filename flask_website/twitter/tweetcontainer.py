from twitter.twitter import getUserTweets, getUserName

class TweetContainer:
  """ TweetContainer class represents a list of tweets from twitter. """
  def __init__(self, screenName):
    self.screenName = screenName
  
  def load(self, count):
    self.userName = getUserName(self.screenName)
    self.tweets = getUserTweets(self.screenName, count)

  def getWorstTweets(self, count):
    newlist = sorted(self.tweets, key=lambda x: x.getSentiment()['neg'], reverse=True)
    return newlist[:count]

  def __dict__(self):
    tweetContainer = {}
    tweetContainer['name'] = self.userName

    # Get all tweets
    tweets = []
    for tweet in self.getWorstTweets(10):
      tweets.append(tweet.__dict__)
    tweetContainer['tweets'] = tweets

    return tweetContainer
    
from twitter.twitter import getUserTweets, getUserName

class TweetContainer:
  """ TweetContainer class represents a list of tweets from twitter. """
  def __init__(self, screenName):
    self.screenName = screenName
  
  def load(self, count):
    self.userName = getUserName(self.screenName)
    self.tweets = getUserTweets(self.screenName, count)

  def getWorstTweets(self, count):
    worstTweets = sorted(self.tweets, key=lambda x: x.getSentiment()['compound'], reverse=False)
    if len(worstTweets) < count:
      return worstTweets[:-1]
    else:
      return worstTweets[:count]

  def toDict(self, count):
    tweetContainer = {}
    tweetContainer["screen_name"] = self.screenName
    tweetContainer["name"] = self.userName

    # Get all tweets
    tweets = []

    # Get the worst tweets
    for tweet in self.getWorstTweets(count):
      tweets.append(tweet.toDict())
    
    tweetContainer["tweets"] = tweets

    return tweetContainer
    
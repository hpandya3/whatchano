from preprocessing.preprocessing import preprocess
from sentiment_analysis.sentiment import getSentiment

class Tweet:
  """ Tweet class represents tweets from twitter and shows sentiment. """

  def __init__(self, tweet):
    self.tweet = tweet
    decodedText = self.tweet.text.encode('ascii', 'ignore').decode('utf-8')
    
    # Calculate sentiment
    self.processedText = preprocess(decodedText)
    self.sentiment = getSentiment(self.processedText)

  def getHashtags(self):
    try:
      return self.tweet.entities['hashtags']
    except AttributeError:
      return None

  def getSymbols(self):
    try:
      return self.tweet.entities['symbols']
    except AttributeError:
      return None

  def getUserMentions(self):
    """Returns screen names"""
    screenNames = []
    
    try:
      for user in self.tweet.entities['user_mentions']:
        screenNames.append(user['screen_name'])

      return screenNames
    except AttributeError:
      return None

  def getUrl(self):
    """Returns simple urls"""
    try:
      return "https://twitter.com/i/status/" + str(self.tweet.id)
    except AttributeError and TypeError:
      return None

  def getRawText(self):
    return self.tweet.text

  def processedText(self):
    return self.processedText

  def getSentiment(self):
    return self.sentiment

  def toDict(self):
    tweet = {}
    tweet["text"] = self.getRawText()
    tweet["url"] = self.getUrl()
    tweet["sentiment"] = self.getSentiment()
    return tweet
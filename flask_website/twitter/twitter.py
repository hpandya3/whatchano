import tweepy
import local_settings as ls
from .tweet import Tweet

# OAuth process, using the keys and tokens
AUTH = tweepy.OAuthHandler(ls.TWITTER_CONSUMER_KEY, ls.TWITTER_CONSUMER_SECRET)
AUTH.set_access_token(ls.TWITTER_ACCESS_TOKEN, ls.TWITTER_ACCESS_TOKEN_SECRET)

# Creation of the actual interface, using authentication
API = tweepy.API(AUTH)

def getUserTweetObjects(screenName, count):
  tweetObjects = []
  tweets = API.user_timeline(screen_name=screenName, count=count)
  if len(tweets) > 0:
    print(tweets[0].user.name) # Persons Name
    print(tweets[0].user.profile_image_url) # Persons Image
    for tweet in tweets:
      tweetObject = Tweet(tweet)
      print('')
      print('Tweet')
      print('Raw Text:' + tweetObject.getRawText())
      print('Compound Sentiment: ' + str(tweetObject.getSentiment()['compound']))
      if tweetObject.getHashtags():
        print(tweetObject.getHashtags())

      if tweetObject.getSymbols():
        print(tweetObject.getSymbols())

      if tweetObject.getUserMentions():
        print(tweetObject.getUserMentions())
      
      if tweetObject.getUrls():
        print(tweetObject.getUrls())
      
      tweetObjects.append(tweetObject)

  return tweetObjects
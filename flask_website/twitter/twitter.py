import tweepy
import local_settings as ls
from preprocessing.preprocessing import preprocess
from sentiment_analysis.sentiment import getSentiment


# OAuth process, using the keys and tokens
AUTH = tweepy.OAuthHandler(ls.TWITTER_CONSUMER_KEY, ls.TWITTER_CONSUMER_SECRET)
AUTH.set_access_token(ls.TWITTER_ACCESS_TOKEN, ls.TWITTER_ACCESS_TOKEN_SECRET)

# Creation of the actual interface, using authentication
API = tweepy.API(AUTH)

def getUserTweets(screenName, count):
  tweets = API.user_timeline(screen_name=screenName, count=count)
  print(tweets[0].user.name) # Persons Name
  print(tweets[0].user.profile_image_url) # Persons Image
  for tweet in tweets:
    decodedText = tweet.text.encode('ascii', 'ignore').decode('utf-8')
    preprocessedText = preprocess(decodedText)
    print(preprocessedText)
    print(getSentiment(preprocessedText))

  return tweets
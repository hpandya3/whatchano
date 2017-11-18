import tweepy
import local_settings as ls

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(ls.TWITTER_CONSUMER_KEY, ls.TWITTER_CONSUMER_SECRET)
auth.set_access_token(ls.TWITTER_ACCESS_TOKEN, ls.TWITTER_ACCESS_TOKEN_SECRET)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Sample method, used to update a status
api.update_status('#internetfreedomhackathon')
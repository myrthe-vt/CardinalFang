import tweepy
import time

from tweepy.models import ResultSet
from keys import keys


consumer_key = keys['consumer_key']
consumer_secret = keys['consumer_secret']
access_token = keys['access_token']
access_token_secret = keys['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Saving tweets that contain the key words
result = api.search(q="Cardinal fang")

#What does it find?
for results in result:
    print(results.text)

#Send the tweet
for s in result:
    username = s.user.screen_name
    if username != "CardinalFangBot":
        m = "@%s CARDINAL FANG @%s!" % (username, username)
        s = api.update_status(m, s.id)
        print("tweet sent!")
        time.sleep(900) #Only tweet once every 15 seconds
    else:
        pass

__author__ = 'dhruv'

import tweepy
from tweepy import OAuthHandler
import json
from presidential_stream import PresidentialListener
import time

consumer_key = "KBGF7ki0I2cRuel9sHcawaox3"
consumer_secret = "3pAk7xc0NE3336vyLtu8MNIRgjohfFxW5uJFvBzf1Vy8xuqgkc"
access_token = "3312575270-0zqo96Ws5bTdWaBnM5n27ZQntWxMU8wutAU9TMA"
access_secret = "WJq1muGi7boFzPx5d8MdhN8VQXHsI8HraEm4aJxla3193"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


# Enable json
@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status

# Status() object
tweepy.models.Status.first_parse = tweepy.models.Status.parse
tweepy.models.Status.parse = parse

# User() object
tweepy.models.User.first_parse = tweepy.models.User.parse
tweepy.models.User.parse = parse

twitter_stream = tweepy.Stream(auth, PresidentialListener())
twitter_stream.filter(track=['#Trump2016'])
__author__ = 'dhruv'

import tweepy
from tweepy import OAuthHandler
import json
from presidential_stream import PresidentialListener
import time

with open("auth/consumer_key") as f:
    consumer_key = f.read()
with open("auth/consumer_secret") as f:
    consumer_secret = f.read()
with open("auth/access_token") as f:
    access_token = f.read()
with open("auth/access_token_secret") as f:
    access_secret = f.read()

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
twitter_stream.filter(track=["Israel", "Carson", "#Trump2016"])
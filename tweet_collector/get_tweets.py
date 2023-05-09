import tweepy
import requests
import logging
#import os 
import pymongo
from dotenv import find_dotenv, dotenv_values 

logging.critical('======================== Hello World! ======================== ')
#bearer_token = os.getenv('BEARER_TOKEN')


ENV = dict(dotenv_values(find_dotenv()))
bearer_token = ENV.get('BEARER_TOKEN')

twitter_client = tweepy.Client(bearer_token=bearer_token)


client = pymongo.MongoClient(host='mongodb', port=27017)
db = client.twitterdb



#import config
#twitter_client = tweepy.Client(bearer_token=config.BEARER_TOKEN)
# - means NOT
search_query = "#ASML -is:retweet"

# option to extract tweets of a particular language add `lang` parameter eg lang:de
cursor = tweepy.Paginator(
    method=twitter_client.search_recent_tweets,
    query=search_query,
    tweet_fields=['author_id', 'created_at', 'public_metrics'],
    user_fields=['username']
).flatten(limit=20)

for tweet in cursor:
     #print(tweet.data)
     db.tweets.insert_one(dict(tweet))
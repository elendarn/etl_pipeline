'''
1. EXTRACT the tweets from mongodb
- connect to the database 
- query the data
2. TRANSFORM the data
- clean the text before?
- sentiment analysis
- maybe transform data types?
3. LOAD the data into postgres
- connect to postgres 
- insert into postgres
'''
import time
from pymongo import MongoClient
from sqlalchemy import create_engine
import logging
from dotenv import find_dotenv, dotenv_values 

logging.basicConfig(filename='debug.log',
                    level=logging.WARNING)

time.sleep(10)


ENV = dict(dotenv_values(find_dotenv()))
post_user = ENV.get('POSTGRES_USER')
post_psw = ENV.get('POSTGRES_PASSWORD')
post_db = ENV.get('POSTGRES_DB')

### create connections to databases (check your mongosb and postgres in python notebooks (or luftdaten))
client = MongoClient(host='mongodb', port=27017)
db = client.twitterdb

pg = create_engine(f'postgresql://{post_user}:{post_psw}@post_box:5432/{post_db}', echo=True)


def extract():  #-> List[dict]
    """extract tweets from mongodb
    """
    extracted_tweets = list(db.tweets.find())
    return extracted_tweets


def transform(extracted_tweets):
    ''' Transforms data: clean text, gets sentiment analysis from text, formats date '''
    ## sentiment analysis tomorrow, basically you pass text and get a number between 0-1 as the sentiment score
    ## add the sentiment to the tweet and store in a dataframe or a dictionary
    transformed_tweets = []
    for tweet in extracted_tweets:
        sentiment_score = 1 # later on you will calculate a sentiment
        # datatype of the tweet: dictionary
        tweet['sentiment'] = sentiment_score # adding a key: value pair with 'sentiment' as the key and the score as the value
        transformed_tweets.append(tweet)
        # transformed_tweets is a list of transformed dictionaries
        return transformed_tweets

def load(transformed_tweets):
    ''' Load final data into postgres'''



extract_tweets = extract()
print(extract_tweets)
print('---------------------------------------------------------------------------------------')
#ransformed_tweets = transform(extracted_tweets)
#load(transformed_tweets)
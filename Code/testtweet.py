__author__ = 'snehi23'

try:
    import json
except ImportError:
    import simplejson as json

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

from pymongo import MongoClient

ACCESS_TOKEN = '234362801-rkG9Z77PgYMf0HltWCGAjYHYOZ3F9nNtF0MiUTo4'
ACCESS_SECRET = 'hceUpRi8iwoL1m2iHYVXcBwj7ZqjEn9ZFp4ilAkQLW3Jw'
CONSUMER_KEY = '632RIUCtQLFgv6DmAFBj2qv1m'
CONSUMER_SECRET = 'mHRJmnrKQKicr4c8ZuhaqhgVXlAVM4k6BzXl02xge0GGDEDZQ5'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_stream = TwitterStream(auth=oauth)
iterator = twitter_stream.statuses.filter(track='#iphone6', language="en")

#twitter_rest_api = Twitter(auth=oauth)
#iterator = twitter_rest_api.search.tweets(q='#India')

tweet_count = 1000
client = MongoClient('localhost',27017)
db = client['twitter_db']
collection = db['twitter_collection']
for tweet in iterator:
    tweet_count -= 1
    print tweet_count
    collection.insert(tweet)
    if tweet_count <= 0:
        break

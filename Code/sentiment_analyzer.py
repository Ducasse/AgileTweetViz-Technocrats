import re


def preprocess_tweet(tweet):
    # Convert to lower case
    tweet = tweet.lower()

    # Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)

    # Convert @username to AT_USER
    tweet = re.sub('@[^\s]+', 'AT_USER', tweet)

    # Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)

    # Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)

    # trim
    tweet = tweet.strip('\'"')
    return tweet


def read_tweets():
    fp = open('data/sampleTweets.txt', 'r')
    line = fp.readline()

    while line:
        processed_tweet = preprocess_tweet(line)
        print processed_tweet
        line = fp.readline()
    fp.close()

__author__ = 'tanmay'

import re
import nltk
import csv


class SentimentAnalyzer:

    def __init__(self, tweets, training_data_file, feature_list_file):
        self.original_tweets = tweets
        self.processed_tweets = []
        for i in tweets:
            new_tweet = self.preprocess_tweet(i)
            self.processed_tweets.append(new_tweet)

        self.wordFeatures = []
        input_file = open(feature_list_file, 'r')
        line = input_file.readline()
        index = 0
        while line:
            print "line -- ", index
            index += 1
            self.wordFeatures.append(line.strip())
            line = input_file.readline()

        self.classifier = self.get_NB_tained_classifer(training_data_file)

    def preprocess_tweet(self, tweet):
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

    def get_NB_tained_classifer(self, training_data_file):
        # read all tweets and labels
        tweet_items = self.get_filtered_training_data(training_data_file)

        tweets = []
        index1 = 0
        for (words, sentiment) in tweet_items:
            print "classifier --- ", index1
            index1 += 1
            words_filtered = [e.lower() for e in words.split() if(self.is_ascii(e))]
            tweets.append((words_filtered, sentiment))

        training_set = nltk.classify.apply_features(self.extract_features, tweets)
        classifier = nltk.NaiveBayesClassifier.train(training_set)
        return classifier

    def extract_features(self, document):
        document_words = set(document)
        features = {}
        index2 = 0
        for word in self.wordFeatures:
            print "extract --- ", index2
            index2 += 1
            word = self.replace_two_or_more(word)
            word = word.strip('\'"?,.')
            features['contains(%s)' % word] = (word in document_words)
        return features

    def replace_two_or_more(self, s):
        # look for three or more repetitions of any charac
        pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
        return pattern.sub(r"\1\1", s)

    def classify(self):
        for i in self.processed_tweets:
            tw = self.processed_tweets[i]
            count = 0
            res = {}
            for t in tw:
                label = self.classifier.classify(self.extract_features(t.split()))
                print label
                # result = {'text': t, 'tweet': self.original_tweets[i][count], 'label': label}
                # res[count] = result

    def get_filtered_training_data(self, trainingDataFile):
        fp = open(trainingDataFile, 'rb')
        reader = csv.reader( fp, delimiter=',', quotechar='"', escapechar='\\' )
        tweet_items = []
        count = 1
        for row in reader:
            processed_tweet = self.preprocess_tweet(row[1])
            sentiment = row[0]
            tweet_item = processed_tweet, sentiment
            tweet_items.append(tweet_item)
            count +=1
        return tweet_items

    def is_ascii(self, word):
        return all(ord(c) < 128 for c in word)


all_tweets = []
classifier_tweets = ['I love this car',
                     'This view is amazing',
                     'I feel great this morning',
                     'I am so excited about the concert',
                     'He is my best friend',
                     'I do not like this car',
                     'This view is terrible',
                     'I feel tired this morning',
                     'I am not looking forward to the concert',
                     'He is my enemy']
analyzer = SentimentAnalyzer(all_tweets, 'training_neatfile.csv', 'feature_list.txt')
analyzer.classify()

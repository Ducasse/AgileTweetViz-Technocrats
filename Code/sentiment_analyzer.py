__author__ = 'tanmay'

import re
import nltk
import csv
import json
import pickle


class SentimentAnalyzer:

    def __init__(self, tweets_file, training_data_file, feature_list_file, dump_file, training_required=True):
        self.name_of_file = tweets_file
        tf = open(self.name_of_file, 'r')
        l = tf.readline()
        tweets_str = ""
        while l:
            tweets_str += l
            l = tf.readline()

        tweets_unicode = json.loads(tweets_str)
        tweets = self.byteify(tweets_unicode)

        self.processed_tweets = []
        for i in tweets:
            new_text = self.preprocess_tweet(i['text'])
            i['text'] = new_text
            self.processed_tweets.append(i)

        self.wordFeatures = []
        input_file = open(feature_list_file, 'r')
        line = input_file.readline()
        while line:
            self.wordFeatures.append(line.strip())
            line = input_file.readline()

        #call training model
        if(training_required):
            self.classifier = self.get_NB_tained_classifer(training_data_file, dump_file)
        else:
            f1 = open(dump_file)
            if f1:
                self.classifier = pickle.load(f1)
                f1.close()
            else:
                self.classifier = self.get_NB_tained_classifer(training_data_file, dump_file)

    def byteify(self, input):
        if isinstance(input, dict):
            return {self.byteify(key):self.byteify(value) for key, value in input.iteritems()}
        elif isinstance(input, list):
            return [self.byteify(element) for element in input]
        elif isinstance(input, unicode):
            return input.encode('utf-8')
        else:
            return input

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

    def get_NB_tained_classifer(self, training_data_file, dump_file):
        # read all tweets and labels
        tweet_items = self.get_filtered_training_data(training_data_file)

        tweets = []
        for (words, sentiment) in tweet_items:
            words_filtered = [e.lower() for e in words.split() if(self.is_ascii(e))]
            tweets.append((words_filtered, sentiment))

        training_set = nltk.classify.apply_features(self.extract_features, tweets)
        classifier = nltk.NaiveBayesClassifier.train(training_set)
        outfile = open(dump_file, 'wb')
        pickle.dump(classifier, outfile)
        outfile.close()
        return classifier

    def extract_features(self, document):
        document_words = set(document)
        features = {}
        # print document
        for word in self.wordFeatures:
            word = self.replace_two_or_more(word)
            word = word.strip('\'"?,.')
            features['contains(%s)' % word] = (word in document_words)
        return features

    def replace_two_or_more(self, s):
        # look for three or more repetitions of any charac
        pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
        return pattern.sub(r"\1\1", s)

    def classify(self):
        index = 0
        for t in self.processed_tweets:
            index += 1
            print "analyzing tweet # ", index
            text = t['text']
            label = self.classifier.classify(self.extract_features(text.split()))
            t['sentiment'] = label
            print text, " : -------- ", label

    def write_file(self):
        file_name = "analyzed_" + self.name_of_file
        f = open(file_name, 'wb')
        f.write(str(self.processed_tweets))
        f.close()


    def get_filtered_training_data(self, training_data_file):
        fp = open(training_data_file, 'rb')
        reader = csv.reader( fp, delimiter=',', quotechar='"', escapechar='\\' )
        tweet_items = []
        for row in reader:
            processed_tweet = self.preprocess_tweet(row[1])
            sentiment = row[0]
            tweet_item = processed_tweet, sentiment
            tweet_items.append(tweet_item)
        return tweet_items

    def is_ascii(self, word):
        return all(ord(c) < 128 for c in word)

analyzer = SentimentAnalyzer('tweets.json', 'training_neatfile.csv', 'feature_list.txt', 'saved_training.pickle', False)
analyzer.classify()
analyzer.write_file()

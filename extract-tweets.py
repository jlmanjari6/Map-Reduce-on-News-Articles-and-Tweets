from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from twitter_credentials import Tokens
import json, re
import pymongo
from pymongo import MongoClient

#to establish connection with mongo db and set the name
#of the database and collection
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['mydb']
collection = db['tweepy_tweets']


# Extraction of tweets using streaming API

class TweetStreamListener(StreamListener):   
    
    
    def __init__(self, api=None):
        super(TweetStreamListener, self).__init__()
       
        self.counter = 0 # a counter to limit the tweets to 1000
        
   
    def on_data(self,data):  
        REG_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE) 
        
        self.counter += 1
        if(self.counter <= 1000):
            data = json.loads(data)
                
            tweet = data['text']

            tweet_no_url = re.sub(r"http\S+", "", tweet) # to remove URLs from tweet
            tweet_no_emoji= REG_EMOJI.sub(r'', tweet_no_url) # to remove emoticons frm the tweet
            #cleaned_tweet = re.sub('[^A-Za-z0-9 ]+', '', tweet_no_emoji)                

            data['text'] = tweet_no_emoji #to replace the tweet with cleaned tweet

            collection.insert_one(data) #to insert the tweets into mongodb 
            return True
        else:
            return False        

    def on_error(self,status):
        print(status)    


if __name__ == "__main__":
    listener = TweetStreamListener()
    auth = OAuthHandler(Tokens.CONSUMER_KEY,
                                Tokens.CONSUMER_SECRET)
    auth.set_access_token(Tokens.ACCESS_TOKEN,
                                Tokens.ACCESS_TOKEN_SECRET)

    stream = Stream(auth, listener)

    stream.filter(track=['Canada' , 'Canada import', 'Canada export',
                          'Canada vehicle sales', 'Canada Education'])


# Extraction of tweets using searching API

import tweepy as twp

api = twp.API(auth)

tweets_info = twp.Cursor(api.search,
                             q=('Canada OR Canada+import OR Canada+export OR Canada+vehicle+sales OR Canada+Education'),
                             lang="en").items(1000)

for item in tweets_info:
    data = item._json                
    tweet = data['text']
    tweet_no_url = re.sub(r"http\S+", "", tweet) # to remove URLs from the tweet
    tweet_no_emoji= re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE).sub(r'', tweet_no_url) # to remove emoticons from tweet
    #cleaned_tweet = re.sub('[^A-Za-z0-9 ]+', '', tweet_no_emoji)                

    data['text'] = tweet_no_emoji # to replace the tweet with cleaned tweet
    collection.insert_one(data) #to insert the tweets into mongodb 


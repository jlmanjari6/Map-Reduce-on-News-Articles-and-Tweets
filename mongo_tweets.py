import pymongo
from pymongo import MongoClient

#to establish connection with mongo db and set the name of the database and collection
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['mydb']
collection = db['tweepy_tweets']

response = ''

mongoresponse = collection.find()

for doc in mongoresponse:
    with open('/home/ubuntu/server/Assign2dw/articles/file_mongo_tweets.txt','ab') as f:
        text = doc['text'] + '\n'
        f.write(text.encode('utf-8'))




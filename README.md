# Cluster Set up
1. I have created an AWS account on Amazon and launched EC2 instance. Using public DNS (IPv4) of my cloud instance and the private key 
file, I have connected to Putty.
2. I have installed Spark on the Ubuntu instance that is created in previous step. Using the steps given in the Tutorial 4 from Labs, 
I have started Master and Slave nodes and started the Spark shell.
3. I have installed MongoDB and Python on the Ubuntu instance by following the tutorials from labs.

# Twitter Data Extraction & Transformation

1. To retrieve tweets from Twitter, I have used Streaming API (Tweepy’s “StreamListener”) and Searching API provided by Twitter. Using these
APIs, I have extracted a total of 2000 tweets with the search words, “Canada”, “Canada import”, “Canada export”, “Canada vehicle sales”, 
“Canada Education”. I have created a Twitter developer account and used the generated Access Tokens and Consumer Keys to access the
APIs and wrote the python script (extract-tweets.py) to extract the tweets along with the metadata such as time, user, profile etc., 
from both the APIs.
2. The text part of the extracted tweets is cleaned by removing emoticons, URLs etc., and are saved to the MongoDB collection along with the metadata.
3. The JSON file containing all the 2000 tweets is extracted from MongoDB using Python script(mongo_tweets.py) and is saved as “file_mongo_tweets.txt” in a separate folder named “articles”

# News Article Data Extraction & Transformation
<p>
I have written python script(extract-articles.py) that opens and reads the two given .sgm files, “reut2-021.sgm” and “reut2-022.sgm”. 
I have not used any external libraries or parsers to extract the files; instead, I have used regex to search the tags <TEXT> and </TEXT>. 
Based on the opening and closing tags, I have separated the files. A total of 1578 files have been generated from both the .sgm files. 
All the generated files are saved automatically in the folder “articles” that is created in the previous step of tweets extraction.
</p>

# Map Reduce on News Articles and Tweets
<p>
I have written PySpark script (map_reduce.py) [5] to perform MapReduce on the data collected to find out the word count of the words 
“oil”, “vehicle”, “university”, “dalhousie”, “expensive”, “good school” or “good schools”, “bad school” or “bad schools” or “poor school”
or “poor schools”, “population”, “bus” or “buses”, “agriculture”, “economy”. The script loops through all the 1579 files (1578 articles 
and tweets file collected from MongoDB) and in each file, the word that is matched with the above set of words, it is appended to a list 
of words. The final list of words is performed with MapReduce to find out the final word count. The word count generated is saved to a 
text file named “wordcount_output.txt”.
</p>

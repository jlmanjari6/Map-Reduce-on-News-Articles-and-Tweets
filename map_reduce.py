import os
import sys
from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("Pyspark Pgm")
sc = SparkContext(conf = conf)

path = '/home/ubuntu/server/Assign2dw/articles/'

search_words = ['oil','vehicle','university','dalhousie','expensive','good school','good schools','bad school','bad schools','poor school',
        'poor schools','population','bus','buses','agriculture','economy']
final_words = []
for file in os.listdir(path):
    contentRDD =sc.textFile(path+file)
    nonempty_lines = contentRDD.filter(lambda x: len(x) > 0)
    words = nonempty_lines.flatMap(lambda x: x.split(' '))
    for word in words.collect():
        if word in search_words:
            final_words.append(word)

final_words = sc.parallelize(list(final_words))
wordcount = final_words.map(lambda x:(x,1)) \
            .reduceByKey(lambda x,y: x+y) \
            .map(lambda x: (x[1], x[0])).sortByKey(False)

wordcount.saveAsTextFile('/home/ubuntu/server/Assign2dw/wordcount_output.txt')
for word in wordcount.collect():
    print(word)

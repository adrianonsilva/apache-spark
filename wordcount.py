import sys
 
from pyspark import SparkContext, SparkConf
 
if __name__ == "__main__":
 
     # create Spark context with Spark configuration
    conf = (SparkConf().setAppName("Word Count - Python")
            .set("spark.hadoop.yarn.resourcemanager.address", "192.168.1.31:8032")
            .set("spark.shuffle.service.enabled", "false")
            .set("spark.dynamicAllocation.enabled", "false"))

    sc = SparkContext(conf=conf)

    # read in text file and split each document into words
    words = sc.textFile("/dataset/count_words.txt").flatMap(lambda line: line.split(" "))

    # count the occurrence of each word
    wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b)

    # remove the output folder
    import subprocess
    output_path = '/dataset/output/'
    subprocess.call(["hdfs", "dfs", "-rm", "-f", output_path])

    #save the results
    wordCounts.saveAsTextFile(output_path)


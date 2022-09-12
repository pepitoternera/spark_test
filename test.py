from pyspark.context import SparkContext

sc = SparkContext('local', 'test')
sc.parallelize([0, 1, 2, 3])

r = sc.wholeTextFiles('*.txt')
print('breakpoint')
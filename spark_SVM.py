import org.apache.spark.sql.SparkSession 
import spark.implicits._

import sys
sys.path.append("/home/phoenix/桌面/home/spark-3.0.0-bin-hadoop2.7/python")

import pyspark
spark = pyspark.sql.SparkSession.builder.appName("SimpleApp").getOrCreate()
sc = spark.sparkContext

df = spark.read.csv('tmdb_5000_movies.csv', inferSchema = True, header = True)
df.printSchema()

df_filter = df.filter(df['production_companies']!='[]')
#出版公司为空的电影

df_whith=df_filter.withColumn('production_companies_tmp', explode(split("production_companies", ",")))
df_whith.select('production_companies_tmp').show(10)
#将出版公司拆为逗号分隔

df_where = df_whith.where(F.col("vote_average")>'6.5')
df_where.printSchema()
#筛选出6.5分以上电影

df_res = df_where.groupBy('production_companies_tmp').agg({"revenue":"sum"}).withColumnRenamed("sum(revenue)","sum_revenue").orderBy(F.desc('sum_revenue'))


df_res.show(10)

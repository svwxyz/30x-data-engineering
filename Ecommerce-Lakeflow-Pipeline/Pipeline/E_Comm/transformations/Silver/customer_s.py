from pyspark import pipelines as dp
from pyspark.sql.functions import * 


@dp.table
def customer_s():
    df = spark.readStream.table('ecomm.bronze.customer_b')
    df = df.withColumn('name',upper(col("name")))
    return df
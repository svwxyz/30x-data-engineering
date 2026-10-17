from pyspark import pipelines as dp
from pyspark.sql.functions import * 

@dp.table(name='ecomlkh.bronze.customer_b')
def customer_B():
    
    df = spark.readStream.table('ecomlkh.src.olist_customers')
    df = df.withColumn("uploaded_at", current_timestamp())
    return df

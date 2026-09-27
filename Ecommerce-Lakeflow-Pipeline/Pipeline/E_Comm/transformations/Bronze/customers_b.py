from pyspark import pipelines as dp 

@dp.table 
def customer_b():
    df = spark.readStream.table('ecomm.src.customers')
    return df
from pyspark import pipelines as dp 

@dp.table(name="ecomm.bronze.customer_b")
def customer_b():
    df = spark.readStream.table('ecomm.src.customers')
    return df
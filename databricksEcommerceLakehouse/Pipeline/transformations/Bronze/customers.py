from pyspark import pipelines as dp 

@dp.table(name='ecomlkh.bronze.customer_b')
def customer_B():
    
    df = spark.readStream.table('ecomlkh.src.olist_customers')
    return df

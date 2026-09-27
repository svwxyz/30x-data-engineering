from pyspark import pipelines as dp 

@dp.table(name='ecomm.bronze.order_b')
def order_b():
    df = spark.readStream.table('ecomm.src.orders')
    return df
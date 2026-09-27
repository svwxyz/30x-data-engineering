from pyspark import pipelines as dp 

@dp.table 
def order_b():
    df = spark.readStream.table('ecomm.src.orders')
    return df
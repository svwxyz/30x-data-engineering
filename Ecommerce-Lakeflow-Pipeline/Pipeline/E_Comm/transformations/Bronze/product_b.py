from pyspark import pipelines as dp 

@dp.table 
def products_b():
    df = spark.readStream.table('ecomm.src.products')
    return df 
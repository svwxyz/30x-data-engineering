from pyspark import pipelines as dp 

@dp.table(name='ecomm.bronze.products_b')
def products_b():
    df = spark.readStream.table('ecomm.src.products')
    return df 
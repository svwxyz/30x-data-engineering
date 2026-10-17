from pyspark import pipelines as dp 

@dp.table(name="ecomlkh.bronze.products_b")
def orders_b():

    df=spark.readStream.table("ecomlkh.src.olist_products")
    return df 
from pyspark import pipelines as dp 

@dp.table(name="ecomlkh.bronze.orders_b")
def orders_b():

    df=spark.readStream.table("ecomlkh.src.olist_orders")
    return df 
from pyspark import pipelines as dp

@dp.table(name="ecomlkh.bronze.orderItems_b")
def order_items():

    df=spark.readStream.table('ecomlkh.src.olist_order_items')
    return df

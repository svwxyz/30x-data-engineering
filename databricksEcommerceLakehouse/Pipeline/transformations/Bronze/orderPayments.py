from pyspark import pipelines as dp

@dp.table(name="ecomlkh.bronze.orderPayments_b")
def order_payments():

    df=spark.readStream.table("ecomlkh.src.olist_order_payments")
    return df
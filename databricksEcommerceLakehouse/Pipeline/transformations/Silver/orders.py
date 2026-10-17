from pyspark import pipelines as dp

rules={
    "rule1":"order_id is not null"
}

@dp.expect_all(rules)
@dp.table(name="ecomlkh.silver.order_s")
def order_s():

    df=spark.readStream.table('ecomlkh.bronze.orders_b')
    df=df.distinct()
    return df
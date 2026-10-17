from pyspark import pipelines as dp

rules={
        "rule1":"order_id is not null"
}

@dp.expect_all(rules)
@dp.table(name="ecomlkh.silver.orderitems_s")
def orderItem():
    df = spark.readStream.table('ecomlkh.bronze.orderitems_b')
    df = df.distinct()
    return df
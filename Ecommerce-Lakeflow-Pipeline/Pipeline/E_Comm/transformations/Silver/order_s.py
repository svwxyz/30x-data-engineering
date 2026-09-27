from pyspark import pipelines as dp
from pyspark.sql.functions import * 

rules= {
            "rule1":"order_id is not null",
            "rule2":"customer_id is not null"}

@dp.table
@dp.expect_all_or_drop(rules)
def order_s():
    df = spark.readStream.table('ecomm.bronze.order_b')
    return df
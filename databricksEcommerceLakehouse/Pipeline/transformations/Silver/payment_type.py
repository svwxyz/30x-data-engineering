from pyspark import pipelines as dp
from pyspark.sql.functions import *

rules={
    "rule1":"order_id is not null"
}

@dp.expect_all(rules)
@dp.table(name="ecomlkh.silver.payment_type")
def order_s():

    df=spark.readStream.table('ecomlkh.bronze.orderpayments_b')
    df=df.withColumns({
                        "payment_type":upper(trim(col("payment_type")))
    }).distinct()
    return df
from pyspark import pipelines as dp
from pyspark.sql.functions import * 

rules= {
            "rule1":"product_id is not null",
            "rule2":"price > 0"
        }

@dp.table
@dp.expect_all_or_drop(rules)
def product_s():
    df = spark.readStream.table('ecomm.bronze.products_b')
    return df
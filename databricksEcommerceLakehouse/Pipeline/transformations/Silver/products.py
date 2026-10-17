from pyspark import pipelines as dp 
from pyspark.sql.functions import *

rules={
            "rules1":"product_id is not null"
}

@dp.expect_all(rules)
@dp.table(name="ecomlkh.silver.products_s")
def products_silver():

    df=spark.readStream.table('ecomlkh.bronze.products_b')
    df=df.withColumns({
            "product_category_name":upper(trim(col("product_category_name")))
    }).distinct()
    return df
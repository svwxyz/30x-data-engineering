from pyspark import pipelines as dp
from pyspark.sql.functions import col, sha2

@dp.materialized_view(name="ecomlkh.gold.dim_products")
def dim_products():

    df = spark.read.table(
        "ecomlkh.silver.products_s"
    )

    df = df.withColumn(
        "product_sk",
        sha2(col("product_id"), 256)
    )

    return df
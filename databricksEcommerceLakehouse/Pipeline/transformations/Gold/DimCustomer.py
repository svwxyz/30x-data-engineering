from pyspark import pipelines as dp
from pyspark.sql.functions import *

@dp.materialized_view(name="ecomlkh.gold.dim_customers")
def dim_customers():

    df = spark.read.table(
        "ecomlkh.silver.customer_s"
    )

    df = df.withColumn(
        "customer_sk",
        sha2(
            concat_ws(
                "||",
                col("customer_id"),
                coalesce(
                    col("__START_AT").cast("string"),
                    lit("UNKNOWN")
                )
            ),
            256
        )
    )

    df = df.withColumn(
        "is_current",
        col("__END_AT").isNull()
    )

    return df
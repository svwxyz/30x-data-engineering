from pyspark import pipelines as dp
from pyspark.sql.functions import (
    sum as spark_sum,
    collect_set,
    sort_array,
    array_join
)

@dp.materialized_view(name="ecomlkh.gold.fact_orders")
def fact_orders():

    orders = spark.read.table(
        "ecomlkh.silver.order_s"
    )

    payments = spark.read.table(
        "ecomlkh.silver.payment_type"
    )

    payment_summary = (
        payments
        .groupBy("order_id")
        .agg(
            spark_sum("payment_value")
                .alias("total_payment_value"),
            array_join(
                sort_array(collect_set("payment_type")),
                ", "
            ).alias("payment_types")
        )
    )

    return orders.join(
        payment_summary,
        on="order_id",
        how="left"
    )
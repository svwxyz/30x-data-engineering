from pyspark import pipelines as dp

from pyspark.sql.functions import (
    col,
    sha2,
    concat_ws,
    coalesce,
    lit
)

@dp.materialized_view(name="ecomlkh.gold.fact_order_items")
def fact_order_items():

    items = spark.read.table(
        "ecomlkh.silver.orderitems_s"
    ).alias("i")

    orders = spark.read.table(
        "ecomlkh.silver.order_s"
    ).alias("o")

    products = spark.read.table(
        "ecomlkh.gold.dim_products"
    ).alias("p")

    customers = spark.read.table(
        "ecomlkh.gold.dim_customers"
    ).alias("c")

    result = (
        items
        .join(orders, "order_id", "inner")
        .join(products, "product_id", "left")
        .join(
            customers,
            (
                (col("o.customer_id") == col("c.customer_id"))
                & (
                    col("o.order_purchase_timestamp")
                    >= col("c.__START_AT")
                )
                & (
                    col("c.__END_AT").isNull()
                    | (
                        col("o.order_purchase_timestamp")
                        < col("c.__END_AT")
                    )
                )
            ),
            "left"
        )
        .select(
            col("i.order_id"),
            col("i.order_item_id"),
            col("c.customer_sk"),
            col("p.product_sk"),
            col("i.seller_id"),
            col("o.order_status"),
            col("o.order_purchase_timestamp"),
            col("i.price"),
            col("i.freight_value")
        )
    )

    return result